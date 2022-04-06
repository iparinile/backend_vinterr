from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.patch_telegram_user import RequestPatchTelegramUserDto
from api.response.telegram_user import ResponseTelegramUserDto
from db.database import DBSession
from db.exceptions import DBTelegramUserNotExistsException, DBDataException, DBIntegrityException
from db.queries import telegram_users as telegram_users_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicTelegramUserNotFound, SanicDBException


class TelegramUserEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, telegram_user_id: int,
                         *args, **kwargs) -> BaseHTTPResponse:

        try:
            telegram_user = telegram_users_queries.get_telegram_user(session, telegram_user_id)
        except DBTelegramUserNotExistsException:
            raise SanicTelegramUserNotFound('Telegram user not found')

        response_model = ResponseTelegramUserDto(telegram_user)

        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_patch(self, request: Request, body: dict, session: DBSession, telegram_user_id: int,
                           *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestPatchTelegramUserDto(body)

        try:
            telegram_user = telegram_users_queries.get_telegram_user(session, telegram_user_id)
        except DBTelegramUserNotExistsException:
            raise SanicTelegramUserNotFound('Telegram user not found')

        telegram_user = telegram_users_queries.patch_color(telegram_user, request_model)

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseTelegramUserDto(telegram_user)

        return await self.make_response_json(body=response_model.dump(), status=200)
