from typing import List

from api.request.create_good import RequestCreateGoodDto
from api.request.patch_good import RequestPatchGoodDto
from db.database import DBSession
from db.exceptions import DBGoodNotExistsException
from db.models import DBGoods, DBVariations


def create_good(session: DBSession, good: RequestCreateGoodDto) -> DBGoods:
    new_good = DBGoods(
        name=good.name,
        article=good.article,
        good_1c_id=good.good_1c_id,
        category_id=good.category_id,
        barcode=good.barcode,
        structure_id=good.structure_id,
        description=good.description,
        is_visible=good.is_visible,
        weight=good.weight
    )

    session.add_model(new_good)

    return new_good


def get_all_goods(session: DBSession, request_params: dict) -> List['DBGoods']:
    goods = session.get_all_goods(request_params)
    return goods


def get_good(session: DBSession, good_id: int):
    db_good = session.get_good_by_id_with_full_info(good_id)

    if len(db_good) == 0:
        raise DBGoodNotExistsException

    return db_good


def get_good_by_id(session: DBSession, good_id: int):
    db_good = session.get_good_by_id(good_id)
    if db_good is None:
        raise DBGoodNotExistsException
    return db_good


def set_default_variation(session: DBSession, db_variation: DBVariations) -> DBGoods:
    db_good = session.get_good_by_id(db_variation.good_id)

    if db_good is None:
        raise DBGoodNotExistsException

    db_good.default_variation = db_variation.id

    return db_good


def patch_good(good: DBGoods, patch_fields_good: RequestPatchGoodDto) -> DBGoods:
    for attr in patch_fields_good.fields:
        if hasattr(patch_fields_good, attr):
            value = getattr(patch_fields_good, attr)
            setattr(good, attr, value)
    return good


def delete_good(good: DBGoods) -> DBGoods:
    good.is_delete = True
    return good
