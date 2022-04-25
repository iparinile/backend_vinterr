from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.patch_customer import RequestPatchCustomerDto
from api.response.customer import ResponseCustomerDto
from db.database import DBSession
from db.exceptions import DBCustomerNotExistsException, DBDataException, DBIntegrityException
from db.queries import customers as customers_queries
from helpers.password import generate_hash, GeneratePasswordHashException
from helpers.psycopg2_exceptions.get_details import get_details_psycopg2_exception
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicCustomerNotFound, SanicPasswordHashException, SanicDBException, \
    SanicDBUniqueFieldException


class CustomerEndpoint(BaseEndpoint):

    async def check_customer_id_in_token(self, token: dict, customer_id: int, response_error_message: str):
        if token.get('customer_id') != customer_id:
            return await self.make_response_json(status=403, message=response_error_message)

    async def method_get(self, request: Request, body: dict, session: DBSession, customer_id: int, token: dict,
                         *args, **kwargs) -> BaseHTTPResponse:

        await self.check_customer_id_in_token(token, customer_id,
                                              response_error_message='You can only get your own data')

        try:
            db_customer = customers_queries.get_customer(session, customer_id=customer_id)
        except DBCustomerNotExistsException:
            raise SanicCustomerNotFound('Customer not found')

        response_model = ResponseCustomerDto(db_customer)

        session.close_session()

        return await self.make_response_json(status=200, body=response_model.dump())

    async def method_patch(self, request: Request, body: dict, session: DBSession, customer_id: int, token: dict,
                           *args, **kwargs) -> BaseHTTPResponse:

        await self.check_customer_id_in_token(token, customer_id,
                                              response_error_message='You can only patch your own data')

        request_model = RequestPatchCustomerDto(body)

        try:
            db_customer = customers_queries.get_customer(session, customer_id=customer_id)
        except DBCustomerNotExistsException:
            raise SanicCustomerNotFound('Customer not found')

        if 'password' in request_model.fields:
            try:
                hashed_password = generate_hash(request_model.password)
            except GeneratePasswordHashException as e:
                raise SanicPasswordHashException(str(e))

            request_model.password = hashed_password

        db_customer = customers_queries.patch_customer(db_customer, request_model)

        try:
            session.commit_session()
        except DBDataException as e:
            raise SanicDBException(str(e))
        except DBIntegrityException as e:
            exception_code, exception_info = get_details_psycopg2_exception(e)
            if exception_code == '23505':
                raise SanicDBUniqueFieldException(exception_info)
            else:
                raise SanicDBException(str(e))

        response_model = ResponseCustomerDto(db_customer)

        session.close_session()

        return await self.make_response_json(status=200, body=response_model.dump())
