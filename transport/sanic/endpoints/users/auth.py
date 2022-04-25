from sanic.request import Request
from sanic.response import BaseHTTPResponse


from api.request.auth_user import RequestAuthUserDto
from api.response.auth import ResponseAuthDto
from db.database import DBSession

from db.exceptions import DBUserNotExistsException
from db.queries import users as users_queries

from helpers.auth import create_token
from helpers.password import check_hash, CheckPasswordHashException

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicUserNotFound, SanicPasswordHashException


class AuthUserEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestAuthUserDto(body)

        try:
            db_user = users_queries.get_user(session, login=request_model.login)
        except DBUserNotExistsException:
            raise SanicUserNotFound('User not found')

        try:
            check_hash(request_model.password, db_user.password)
        except CheckPasswordHashException:
            raise SanicPasswordHashException('Wrong password', status_code=401)

        payload = {
            'user_id': db_user.id,
            'role': 'admin'
        }

        token = create_token(payload)
        response_body = {
            'user_id': db_user.id,
            'Authorization': token
        }

        response_model = ResponseAuthDto(response_body, is_input_dict=True)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=200)
