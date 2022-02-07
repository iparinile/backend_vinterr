from api.request import RequestCreateUserDto
from db.database import DBSession
from db.exceptions import DBUserExistsException, DBUserNotExistsException
from db.models import DBUsers


def create_user(session: DBSession, user: RequestCreateUserDto, hashed_password: bytes) -> DBUsers:
    new_user = DBUsers(
        login=user.login,
        password=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name
    )

    if session.get_user_by_login(new_user.login) is not None:
        raise DBUserExistsException

    session.add_model(new_user)

    return new_user


def get_user(session: DBSession, login: str = None) -> DBUsers:
    db_user = None

    if login is not None:
        db_user = session.get_user_by_login(login)

    if db_user is None:
        raise DBUserNotExistsException
    return db_user
