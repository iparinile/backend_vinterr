from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.patch_user import RequestPatchUserDto
from api.response import ResponseUserDto
from db.database import DBSession
from db.exceptions import DBUserNotExistsException, DBDataException, DBIntegrityException
from db.queries import users as users_queries
from helpers.password import generate_hash, GeneratePasswordHashException
from helpers.psycopg2_exceptions.get_details import get_details_psycopg2_exception
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicUserNotFound, SanicPasswordHashException, SanicDBException, \
    SanicDBUniqueFieldException


class UserEndpoint(BaseEndpoint):

    async def check_user_id_in_token(self, token: dict, user_id: int, response_error_message: str):
        if token.get('user_id') != user_id:
            return await self.make_response_json(status=403, message=response_error_message)

    async def method_get(self, request: Request, body: dict, session: DBSession, user_id: int, token: dict,
                         *args, **kwargs) -> BaseHTTPResponse:

        await self.check_user_id_in_token(token, user_id, response_error_message='You can only get your own data')

        try:
            db_user = users_queries.get_user(session, user_id=user_id)
        except DBUserNotExistsException:
            raise SanicUserNotFound('User not found')

        response_model = ResponseUserDto(db_user)

        session.close_session()

        return await self.make_response_json(status=200, body=response_model.dump())

    async def method_patch(self, request: Request, body: dict, session: DBSession, user_id: int, token: dict,
                           *args, **kwargs) -> BaseHTTPResponse:

        await self.check_user_id_in_token(token, user_id, response_error_message='You can only patch your own data')

        request_model = RequestPatchUserDto(body)

        try:
            db_user = users_queries.get_user(session, user_id=user_id)
        except DBUserNotExistsException:
            raise SanicUserNotFound('User not found')

        if 'password' in request_model.fields:
            try:
                hashed_password = generate_hash(request_model.password)
            except GeneratePasswordHashException as e:
                raise SanicPasswordHashException(str(e))

            request_model.password = hashed_password

        db_user = users_queries.patch_user(db_user, request_model)

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

        response_model = ResponseUserDto(db_user)

        session.close_session()

        return await self.make_response_json(status=200, body=response_model.dump())
