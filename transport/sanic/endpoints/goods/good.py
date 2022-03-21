from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.category import ResponseCategoryDto
from api.response.color import ResponseColorDto
from api.response.directory_item import ResponseStructureDto, ResponseSizeDto
from api.response.good import ResponseGoodDto
from api.response.image import ResponseImageDto
from api.response.variation import ResponseVariationDto
from db.database import DBSession
from db.exceptions import DBGoodNotExistsException
from db.queries import goods as goods_queries
from db.queries import variations as variations_queries
from db.queries import images as images_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicGoodNotFound


class GoodEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, good_id: int,
                         *args, **kwargs) -> BaseHTTPResponse:

        try:
            db_goods, db_categories, db_structures = goods_queries.get_good(session, good_id)
        except DBGoodNotExistsException:
            raise SanicGoodNotFound('Good not found')

        valid_goods = ResponseGoodDto(db_goods).dump()
        valid_category = ResponseCategoryDto(db_categories).dump()
        valid_structure = ResponseStructureDto(db_structures).dump()

        valid_goods['category_name'] = valid_category['name']
        valid_goods['structure_name'] = valid_structure['name']
        valid_goods['variations'] = []

        records = variations_queries.get_variations_for_good(session, valid_goods['id'])

        if len(records) != 0:
            for db_variations, db_colors, db_sizes in records:
                valid_variation = ResponseVariationDto(db_variations).dump()
                valid_color = ResponseColorDto(db_colors).dump()
                valid_size = ResponseSizeDto(db_sizes).dump()
                valid_variation['color'] = valid_color
                valid_variation['size_name'] = valid_size['name']

                images = images_queries.get_images_for_variation(session, valid_variation['id'])
                if len(images) > 0:
                    response_image = ResponseImageDto(images, many=True)
                    valid_variation['images'] = response_image.dump()
                else:
                    valid_variation['images'] = []

                valid_goods['variations'].append(valid_variation)

        return await self.make_response_json(body=valid_goods, status=200)
