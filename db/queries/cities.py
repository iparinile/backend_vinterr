from db.database import DBSession
from db.models import DBCities


def create_city(session: DBSession, name: str) -> DBCities:
    new_city = DBCities(
        name=name
    )

    db_city = session.get_city_by_name(name)
    if db_city is not None:
        return db_city

    session.add_model(new_city)

    return new_city
