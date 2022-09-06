from typing import List

from api.request.create_directory_item import RequestCreateProductsCareDto
from db.database import DBSession
from db.exceptions import DBProductsCareExistsException, DBProductsCareNotExistsException
from db.models.products_care import DBProductsCare


def create_products_care(session: DBSession, products_care: RequestCreateProductsCareDto) -> DBProductsCare:
    new_products_care = DBProductsCare(
        name=products_care.name
    )

    if session.get_products_care_by_name(new_products_care.name) is not None:
        raise DBProductsCareExistsException

    session.add_model(new_products_care)

    return new_products_care


def get_all_products_care(session: DBSession) -> List['DBProductsCare']:
    products_care = session.get_all_products_care()
    return products_care


def get_products_care(session: DBSession, products_care_id: int) -> DBProductsCare:
    products_care = session.get_products_care_by_id(products_care_id)
    if products_care is None:
        raise DBProductsCareNotExistsException
    return products_care


def patch_products_care(products_care: DBProductsCare, new_name: str) -> DBProductsCare:
    products_care.name = new_name
    return products_care


def delete_products_care(session: DBSession, products_care_id: int) -> None:
    session.delete_products_care(products_care_id)