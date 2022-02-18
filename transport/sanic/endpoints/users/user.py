from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response import ResponseUserDto
from db.database import DBSession
from db.exceptions import DBUserNotExistsException
from db.queries import users as users_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicUserNotFound


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

        return await self.make_response_json(status=200, body=response_model.dump())