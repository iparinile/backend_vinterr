from api.request.create_telegram_user import RequestCreateTelegramUserDto
from api.request.patch_telegram_user import RequestPatchTelegramUserDto
from db.database import DBSession
from db.exceptions import DBTelegramUserExistsException, DBTelegramUserNotExistsException
from db.models import DBTelegramUsers


def create_telegram_user(session: DBSession, telegram_user: RequestCreateTelegramUserDto) -> DBTelegramUsers:
    new_telegram_user = DBTelegramUsers(
        chat_id=telegram_user.chat_id,
        status_id=10
    )

    if session.get_telegram_user_by_id(new_telegram_user.chat_id) is not None:
        raise DBTelegramUserExistsException

    session.add_model(new_telegram_user)

    return new_telegram_user


def get_telegram_user(session: DBSession, telegram_user_id) -> DBTelegramUsers:
    db_telegram_user = session.get_telegram_user_by_id(telegram_user_id)

    if db_telegram_user is None:
        raise DBTelegramUserNotExistsException

    return db_telegram_user


def patch_color(
        telegram_user: DBTelegramUsers,
        patch_fields_telegram_user: RequestPatchTelegramUserDto
) -> DBTelegramUsers:
    for attr in patch_fields_telegram_user.fields:
        if hasattr(patch_fields_telegram_user, attr):
            value = getattr(patch_fields_telegram_user, attr)
            setattr(telegram_user, attr, value)
    return telegram_user
