from db.database import DBSession
from db.exceptions import DBDeliveryTypeNotExistsException
from db.models import DBDeliveryTypes


def get_delivery_type_name_by_id(session: DBSession, delivery_type_id: int) -> DBDeliveryTypes:
    db_delivery_type = session.get_delivery_type_by_id(delivery_type_id)

    if db_delivery_type is None:
        raise DBDeliveryTypeNotExistsException

    return db_delivery_type
