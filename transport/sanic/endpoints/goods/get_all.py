from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.goods_all import ResponseGoodsAllDto
from db.database import DBSession
from db.queries import goods as goods_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicInvalidRequestParameterException


class GetAllGoodsEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        valid_request_params = ["category_id", "color_id", "size_id"]
        request_params = request.args
        for param_name in request_params.keys():
            if param_name not in valid_request_params:
                raise SanicInvalidRequestParameterException

        records = goods_queries.get_all_goods(session, request_params)

        response_body = dict()
        for db_goods, db_variations, db_colors, db_sizes, db_images, db_structures, db_products_care in records:
            if db_goods.id not in response_body.keys():
                if db_structures is not None:
                    db_goods.structure = db_structures.name
                else:
                    db_goods.structure = None
                if db_products_care is not None:
                    db_goods.product_care = db_products_care.name
                else:
                    db_goods.product_care = None
                # valid_goods = ResponseGoodDto(db_goods).dump()
                db_goods.variations = dict()
                db_goods.colors = dict()
                db_goods.variations_to_show = dict()
                response_body[db_goods.id] = db_goods
            if db_variations is not None:
                if db_variations.id not in response_body[db_goods.id].variations.keys():
                    db_variations.images = []
                    response_body[db_goods.id].variations[db_variations.id] = db_variations
                    colors_dict = response_body[db_goods.id].colors
                    if db_colors.id not in colors_dict.keys():
                        db_colors.sizes = dict()
                        response_body[db_goods.id].colors[db_colors.id] = db_colors

                    variations_to_show_dict = response_body[db_goods.id].variations_to_show
                    if db_colors.id not in variations_to_show_dict.keys():
                        response_body[db_goods.id].variations_to_show[db_colors.id] = db_variations.id

                    if db_sizes.id not in response_body[db_goods.id].colors[db_colors.id].sizes:
                        response_body[db_goods.id].colors[db_colors.id].sizes[db_sizes.id] = db_sizes

                if db_images is not None:
                    response_body[db_goods.id].variations[db_variations.id].images.append(db_images)

        response_body = [good for good in response_body.values()]
        for good in response_body:
            good.colors = [color for color in good.colors.values()]
            good.variations = [variation for variation in good.variations.values()]
            good.variations_to_show = [variation for variation in good.variations_to_show.values()]

            for color in good.colors:
                try:
                    color.sizes = [size for size in color.sizes.values()]
                except AttributeError:
                    pass
        response = ResponseGoodsAllDto(response_body, many=True)

        session.close_session()

        return await self.make_response_json(status=200, body=response.dump())
