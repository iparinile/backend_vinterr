from db.database import DBSession
from db.models import DBStreets


def create_city(session: DBSession, name: str) -> DBStreets:
    new_street = DBStreets(
        name=name
    )

    db_street = session.get_street_by_name(name)
    if db_street is not None:
        return db_street

    session.add_model(new_street)

    return new_street
