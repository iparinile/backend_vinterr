import os
import uuid

import requests
from dotenv import load_dotenv
from sanic.request import Request
from sanic.response import BaseHTTPResponse

from db.database import DBSession
from db.exceptions import DBOrderNotExistsException, DBDataException, DBIntegrityException
from db.queries import orders as orders_queries
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
        register_payment_sberbank_url = "https://securepayments.sberbank.ru/payment/rest/getOrderStatusExtended.do?"
        register_payment_sberbank_url += f"userName={sberbank_username}&password={sberbank_password}&"
        register_payment_sberbank_url += f"orderId={db_order.sberbank_id}"

        sberbank_response = requests.get(register_payment_sberbank_url)
        sberbank_response_body = sberbank_response.json()

        sberbank_response_body["order_id"] = db_order.id

        if sberbank_response_body["actionCode"] == 0:
            db_order.is_payed = True

            try:
                session.commit_session(need_close=True)
            except (DBDataException, DBIntegrityException) as e:
                raise SanicDBException(str(e))

        return await self.make_response_json(body=sberbank_response_body, status=200)
