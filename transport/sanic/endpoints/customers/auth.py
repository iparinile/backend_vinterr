from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.auth_customer import RequestAuthCustomerDto
from api.response.auth import ResponseAuthDto
from db.database import DBSession
from db.exceptions import DBCustomerNotExistsException
from db.queries import customers as customers_queries
from helpers.auth import create_token
from helpers.password import check_hash, CheckPasswordHashException
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicCustomerNotFound, SanicPasswordHashException


class AuthCustomerEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestAuthCustomerDto(body)

        try:
            db_customer = customers_queries.get_customer(session, login=request_model.login)
        except DBCustomerNotExistsException:
            raise SanicCustomerNotFound('Customer not found')

        try:
            check_hash(request_model.password, db_customer.password)
        except CheckPasswordHashException:
            raise SanicPasswordHashException('Wrong password', status_code=401)

        payload = {
            'customer_id': db_customer.id,
            'role': 'customer'
        }

        token = create_token(payload)
        response_body = {
            'customer_id': db_customer.id,
            'Authorization': token
        }

        response_model = ResponseAuthDto(response_body, is_input_dict=True)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=200)
