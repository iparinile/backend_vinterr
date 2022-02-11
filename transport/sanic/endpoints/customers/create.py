from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.create_customer import RequestCreateCustomerDto
from api.response.customer import ResponseCustomerDto
from db.exceptions import DBCustomerLoginExistsException, DBDataException, DBIntegrityException, \
    DBCustomerEmailExistsException, DBCustomerPhoneNumberExistsException
from db.queries import customers as customers_queries
from helpers.password import generate_hash, GeneratePasswordHashException
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicPasswordHashException, SanicCustomerConflictException, SanicDBException


class CreateCustomerEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateCustomerDto(body)

        try:
            hashed_password = generate_hash(request_model.password)
        except GeneratePasswordHashException as e:
            raise SanicPasswordHashException(str(e))

        try:
            db_customer = customers_queries.create_customer(session, request_model, hashed_password)
        except DBCustomerLoginExistsException:
            raise SanicCustomerConflictException('Login is busy')
        except DBCustomerEmailExistsException:
            raise SanicCustomerConflictException('Email is busy')
        except DBCustomerPhoneNumberExistsException:
            raise SanicCustomerConflictException('Phone number is busy')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseCustomerDto(db_customer)

        return await self.make_response_json(body=response_model.dump(), status=201)
