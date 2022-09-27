import json
import os

import requests
from dotenv import load_dotenv
from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.register_payment import RequestRegisterPaymentDto
from api.response.register_payment import ResponseRegisterPaymentDto
from db.database import DBSession
from db.exceptions import DBOrderNotExistsException, DBOrderExistsException, DBDataException, DBIntegrityException
from db.queries import orders as orders_queries
from db.queries import variations as variations_queries
from db.queries import variation_in_orders as variation_in_orders_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicOrderNotFound, SanicSberbankIdConflictException, SanicDBException, \
    SanicRegisterPaymentException

load_dotenv()


class RegisterPaymentsEndpoint(BaseEndpoint):
    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        request_model = RequestRegisterPaymentDto(body)

        try:
            db_order = orders_queries.get_order(session, request_model.order_id)[0]
        except DBOrderNotExistsException:
            raise SanicOrderNotFound('Order not found')

        request_model.amount = request_model.amount * 100  # Без учета копеек

        order_bundle = {"cartItems": {"items": []}}

        variations_in_order = variation_in_orders_queries.get_variations_in_order_by_order_id(session, db_order.id)
        for db_variation_in_order in variations_in_order:
            db_variation = variations_queries.get_variations_by_id(session, db_variation_in_order.variation_id)

            order_bundle["cartItems"]["items"].append({
                "positionId": db_variation_in_order.id,
                "name": db_variation.name,
                "quantity": {
                    "value": str(db_variation_in_order.amount),
                    "measure": "шт."
                },
                "itemCode": db_variation.id,
                "tax": {
                    "taxType": 0,
                    "taxSum": 0
                },
                "itemPrice": db_variation_in_order.current_price * 100,
                "itemAttributes": {
                    "attributes": [
                        {"name": "paymentMethod", "value": "1"},
                        {"name": "paymentObject", "value": "1"}
                    ]
                }
            })

        if db_order.delivery_type_id != 1:
            order_bundle["cartItems"]["items"].append("")


        sberbank_username = os.getenv("sber_username")
        sberbank_password = os.getenv("sber_password")
        register_payment_sberbank_url = "https://securepayments.sberbank.ru/payment/rest/register.do?"
        register_payment_sberbank_url += f"userName={sberbank_username}&password={sberbank_password}&"
        register_payment_sberbank_url += f"orderNumber={db_order.id}&amount={request_model.amount}&"
        register_payment_sberbank_url += f"returnUrl={request_model.return_url}&failUrl={request_model.fail_url}&"
        register_payment_sberbank_url += f"orderBundle={json.dumps(order_bundle)}"

        sberbank_response = requests.get(register_payment_sberbank_url)
        sberbank_response_body = sberbank_response.json()

        if "errorCode" in sberbank_response_body.keys():
            raise SanicRegisterPaymentException(sberbank_response_body['errorMessage'])

        try:
            db_order = orders_queries.patch_sberbank_id(session, db_order, sberbank_response_body["orderId"])
        except DBOrderExistsException:
            raise SanicSberbankIdConflictException(message="Sberbank_id already exists")

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_body = {
            "order_id": db_order.id,
            "sberbank_order_id": sberbank_response_body["orderId"],
            "payment_form_url": sberbank_response_body["formUrl"],
            "amount": request_model.amount,
        }
        response_model = ResponseRegisterPaymentDto(response_body, is_input_dict=True)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=200)
