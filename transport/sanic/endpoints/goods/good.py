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

        valid_good = ResponseGoodDto(db_goods).dump()
        valid_category = ResponseCategoryDto(db_categories).dump()
        valid_structure = ResponseStructureDto(db_structures).dump()

        valid_good['category_name'] = valid_category['name']
        valid_good['structure_name'] = valid_structure['name']
        valid_good['variations'] = []
        valid_good['variations_to_show'] = dict()

        records = variations_queries.get_variations_for_good(session, valid_good['id'])

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
                    valid_variation['images'].sort()
                else:
                    valid_variation['images'] = []

                valid_good['variations'].append(valid_variation)

                if db_variations.color_id not in valid_good['variations_to_show'].keys():
                    valid_good['variations_to_show'][db_variations.color_id] = db_variations.id

            valid_good['variations_to_show'] = [variation_id for variation_id in
                                                valid_good['variations_to_show'].values()]

        session.close_session()

        return await self.make_response_json(body=valid_good, status=200)
