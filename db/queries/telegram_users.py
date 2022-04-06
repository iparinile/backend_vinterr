from api.request.create_telegram_user import RequestCreateTelegramUserDto
from db.database import DBSession
from db.exceptions import DBTelegramUserExistsException
from db.models import DBTelegramUsers


def create_telegram_user(session: DBSession, telegram_user: RequestCreateTelegramUserDto) -> DBTelegramUsers:
    new_telegram_user = DBTelegramUsers(
        chat_id=telegram_user.chat_id,
        status_id=1
    )

    if session.get_telegram_user_by_id(new_telegram_user.chat_id) is not None:
        raise DBTelegramUserExistsException

    session.add_model(new_telegram_user)

    return new_telegram_user
