from sanic.request import Request
from sanic.response import BaseHTTPResponse


from api.request import RequestCreateUserDto
from api.response import ResponseUserDto

from db.queries import users as users_queries
from db.exceptions import DBUserExistsException, DBDataException, DBIntegrityException

from helpers.password import generate_hash, GeneratePasswordHashException

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicPasswordHashException, SanicUserConflictException, SanicDBException


class CreateUserEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateUserDto(body)

        try:
            hashed_password = generate_hash(request_model.password)
        except GeneratePasswordHashException as e:
            raise SanicPasswordHashException(str(e))

        try:
            db_user = users_queries.create_user(session, request_model, hashed_password)
        except DBUserExistsException:
            raise SanicUserConflictException('Login is busy')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseUserDto(db_user)

        return await self.make_response_json(body=response_model.dump(), status=201)
