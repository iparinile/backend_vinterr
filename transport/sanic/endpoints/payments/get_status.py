import os
import uuid
from datetime import datetime

import requests
from dateutil.tz import tzlocal
from dotenv import load_dotenv
from sanic.request import Request
from sanic.response import BaseHTTPResponse

from db.database import DBSession
from db.exceptions import DBOrderNotExistsException, DBDataException, DBIntegrityException
from db.queries import orders as orders_queries
from helpers.telegram_bot.send_message import send_message_to_chat
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicOrderNotFound, SanicDBException

load_dotenv()


class GetStatusPaymentsEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, sberbank_order_id: uuid,
                         *args, **kwargs) -> BaseHTTPResponse:
        try:
            db_order = orders_queries.get_order_by_sberbank_id(session, str(sberbank_order_id))
        except DBOrderNotExistsException:
            raise SanicOrderNotFound('Order not found')

        sberbank_username = os.getenv("sber_username")
        sberbank_password = os.getenv("sber_password")
        register_payment_sberbank_url = "https://3dsec.sberbank.ru/payment/rest/getOrderStatusExtended.do?"
        register_payment_sberbank_url += f"userName={sberbank_username}&password={sberbank_password}&"
        register_payment_sberbank_url += f"orderId={db_order.sberbank_id}"

        sberbank_response = requests.get(register_payment_sberbank_url)
        sberbank_response_body = sberbank_response.json()

        sberbank_response_body["order_id"] = db_order.id

        if sberbank_response_body["actionCode"] == 0:
            db_order.is_payed = True

            try:
                session.commit_session()
            except (DBDataException, DBIntegrityException) as e:
                raise SanicDBException(str(e))

            pay_data = sberbank_response_body["depositedDate"] / 1000
            pay_data = datetime.utcfromtimestamp(pay_data)
            pay_data = datetime(
                year=pay_data.year,
                month=pay_data.month,
                day=pay_data.day,
                hour=pay_data.hour + 5,
                minute=pay_data.minute,
                second=pay_data.second
            )

            pay_data = pay_data.strftime('%H:%M - %d.%m.%Y')
            message = f"""
Оплачен заказ №{db_order.id} в {pay_data}

"""

            send_message_to_chat(chat_id=os.getenv("telegram_chat_id"), message=message)

        session.close_session()

        return await self.make_response_json(body=sberbank_response_body, status=200)
