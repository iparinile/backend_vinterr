from api.request.create_good import RequestCreateGoodDto
from db.database import DBSession
from db.models import DBGoods


def create_good(session: DBSession, good: RequestCreateGoodDto) -> DBGoods:
    new_good = DBGoods(
        name=good.name,
        article=good.article,
        good_1c_id=good.good_1c_id,
        category_id=good.category_id,
        barcode=good.barcode,
        structure_id=good.structure_id
    )

    session.add_model(new_good)

    return new_good
