from typing import List

from api.request.create_variation import RequestCreateVariationDto
from api.request.patch_variations import RequestPatchVariationDto
from db.database import DBSession
from db.exceptions import DBVariationsForGoodNotExistsException, DBVariationNotExistsException, DBVariationNegativeRest
from db.models import DBVariations


def create_variation(session: DBSession, variation: RequestCreateVariationDto) -> DBVariations:
    new_variation = DBVariations(
        good_id=variation.good_id,
        name=variation.name,
        color_id=variation.color_id,
        size_id=variation.size_id,
        price=variation.price,
        discounted_price=variation.discounted_price,
        variation_1c_id=variation.variation_1c_id,
        amount=variation.amount,
        barcode=variation.barcode,
        is_sale=variation.is_sale,
        is_new=variation.is_new
    )

    session.add_model(new_variation)

    return new_variation


def get_all_variations(session: DBSession) -> List['DBVariations']:
    variations = session.get_all_variations()
    return variations


def get_variations_for_good(session: DBSession, good_id: int) -> List['DBVariations']:
    records = session.get_variations_by_good_id(good_id)

    return records


def get_variations_by_id(session: DBSession, variation_id: int) -> DBVariations:
    db_variation = session.get_variation_by_id(variation_id)

    if db_variation is None:
        raise DBVariationNotExistsException

    return db_variation


def get_variations_by_id_with_full_info(session: DBSession, variation_id: int) -> DBVariations:
    record = session.get_variation_by_id_with_full_info(variation_id)

    if record is None:
        raise DBVariationNotExistsException

    return record


def buying_variations(db_variation: DBVariations, amount: int) -> DBVariations:
    variation_rest = db_variation.amount
    variation_rest = variation_rest - amount
    if variation_rest < 0:
        raise DBVariationNegativeRest

    db_variation.amount = variation_rest
    return db_variation


def patch_variation(variation: DBVariations, patch_fields_variation: RequestPatchVariationDto) -> DBVariations:
    for attr in patch_fields_variation.fields:
        if hasattr(patch_fields_variation, attr):
            value = getattr(patch_fields_variation, attr)
            setattr(variation, attr, value)
    return variation
