from typing import List

from api.request.create_good import RequestCreateGoodDto
from db.database import DBSession
from db.models import DBVariations


def create_variations(session: DBSession, good: RequestCreateGoodDto) -> List['DBVariations']:
    variations_list = []
    for variation in good.variations:
        new_variation = DBVariations(
            good_id=1,
            name=variation['name'],
            color_id=variation['color_id'],
            size_id=variation['size_id'],
            price=variation['price'],
            variation_1c_id=variation['variation_1c_id'],
            amount=variation['amount'],
            barcode=variation['barcode'],
            is_sale=variation['is_sale'],
            is_new=variation['is_new']
        )

        session.add_model(new_variation)
        variations_list.append(new_variation)

    return variations_list
