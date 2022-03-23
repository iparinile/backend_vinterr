from typing import List

from api.request.create_directory_item import RequestCreateDeliveryTypeDto
from db.database import DBSession
from db.exceptions import DBDeliveryTypeNotExistsException, DBDeliveryTypeExistsException
from db.models import DBDeliveryTypes


def get_delivery_type_name_by_id(session: DBSession, delivery_type_id: int) -> DBDeliveryTypes:
    db_delivery_type = session.get_delivery_type_by_id(delivery_type_id)

    if db_delivery_type is None:
        raise DBDeliveryTypeNotExistsException

    return db_delivery_type


def create_delivery_type(session: DBSession, delivery_type: RequestCreateDeliveryTypeDto) -> DBDeliveryTypes:
    new_delivery_type = DBDeliveryTypes(
        name=delivery_type.name
    )

    if session.get_delivery_type_by_name(new_delivery_type.name) is not None:
        raise DBDeliveryTypeExistsException

    session.add_model(new_delivery_type)

    return new_delivery_type


def get_all_delivery_types(session: DBSession) -> List['DBDeliveryTypes']:
    delivery_type = session.get_all_delivery_types()
    return delivery_type
