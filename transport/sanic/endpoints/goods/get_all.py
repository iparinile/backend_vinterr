from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.color import ResponseColorDto
from api.response.directory_item import ResponseSizeDto
from api.response.good import ResponseGoodDto
from api.response.image import ResponseImageDto
from api.response.variation import ResponseVariationDto
from db.database import DBSession
from db.queries import goods as goods_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllGoodsEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        records = goods_queries.get_all_goods(session)

        response_body = dict()
        for db_goods, db_variations, db_colors, db_sizes, db_images in records:
            if db_goods.id not in response_body.keys():
                valid_goods = ResponseGoodDto(db_goods).dump()
                valid_goods['variations'] = dict()
                valid_goods['colors'] = dict()
                response_body[valid_goods['id']] = valid_goods
            if db_variations is not None:
                if db_variations not in response_body[db_goods.id]['variations'].keys():
                    valid_variation = ResponseVariationDto(db_variations).dump()
                    valid_color = ResponseColorDto(db_colors).dump()
                    valid_size = ResponseSizeDto(db_sizes).dump()
                    valid_variation['images'] = []
                    response_body[db_goods.id]['variations'][db_variations.id] = valid_variation
                    colors_dict = response_body[db_goods.id]['colors']
                    if valid_color['id'] not in colors_dict.keys():
                        valid_color['sizes'] = dict()
                        response_body[db_goods.id]['colors'][valid_color['id']] = valid_color

                    if valid_size['id'] not in response_body[db_goods.id]['colors'][valid_color['id']]['sizes']:
                        response_body[db_goods.id]['colors'][valid_color['id']]['sizes'][valid_size['id']] = valid_size

                if db_images is not None:
                    valid_image = ResponseImageDto(db_images)
                    response_body[db_goods.id]['variations'][db_variations.id].append(valid_image)

        response_body = [good for good in response_body.values()]
        for good in response_body:
            good['colors'] = [color for color in good['colors'].values()]
            good['variations'] = [variation for variation in good['variations'].values()]

            for color in good['colors']:
                color['sizes'] = [size for size in color['sizes'].values()]

        return await self.make_response_json(status=200, body=response_body)
