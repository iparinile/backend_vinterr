from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.create_telegram_user import RequestCreateTelegramUserDto
from api.response.telegram_user import ResponseTelegramUserDto

from db.queries import telegram_users as telegram_users_queries
from db.exceptions import DBDataException, DBIntegrityException, DBTelegramUserExistsException

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicTelegramUserConflictException


class CreateTelegramUserEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateTelegramUserDto(body)

        try:
            db_telegram_user = telegram_users_queries.create_telegram_user(session, request_model)
        except DBTelegramUserExistsException:
            raise SanicTelegramUserConflictException('Chat_id is busy')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseTelegramUserDto(db_telegram_user)

        return await self.make_response_json(body=response_model.dump(), status=201)
