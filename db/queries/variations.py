from typing import List

from api.request.create_variation import RequestCreateVariationDto
from db.database import DBSession
from db.exceptions import DBVariationsForGoodNotExistsException
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


def get_variations_for_good(session: DBSession, good_id: int) -> DBVariations:
    variations = session.get_variations_by_good_id(good_id)
    if variations is None:
        raise DBVariationsForGoodNotExistsException
    return variations