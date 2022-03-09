from db.database import DBSession
from db.models import DBRegions


def create_region(session: DBSession, name: str) -> DBRegions:
    new_region = DBRegions(
        name=name
    )

    db_region = session.get_region_by_name(name)
    if db_region is not None:
        return db_region

    session.add_model(new_region)

    return new_region
