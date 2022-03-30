from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.color import ResponseColorDto
from api.response.directory_item import ResponseSizeDto
from api.response.image import ResponseImageDto
from api.response.variation import ResponseVariationDto
from db.database import DBSession
from db.exceptions import DBVariationNotExistsException
from db.queries import variations as variations_queries
from db.queries import images as images_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicVariationNotFound


class GetVariationEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, variation_id: int,
                         *args, **kwargs) -> BaseHTTPResponse:

        try:
            record = variations_queries.get_variations_by_id_with_full_info(session, variation_id)
        except DBVariationNotExistsException:
            raise SanicVariationNotFound('Variation not found')

        db_variation, db_color, db_size = record
        valid_variation = ResponseVariationDto(db_variation).dump()
        valid_color = ResponseColorDto(db_color).dump()
        valid_size = ResponseSizeDto(db_size).dump()

        valid_variation['size_name'] = valid_size['name']
        valid_variation['color'] = valid_color

        images = images_queries.get_images_for_variation(session, valid_variation['id'])
        if len(images) > 0:
            response_image = ResponseImageDto(images, many=True)
            valid_variation['images'] = response_image.dump()
        else:
            valid_variation['images'] = []

        return await self.make_response_json(body=valid_variation, status=200)
