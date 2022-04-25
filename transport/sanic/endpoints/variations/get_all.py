from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.image import ResponseImageDto
from api.response.variation import ResponseVariationDto
from db.database import DBSession
from db.queries import images as images_queries
from db.queries import variations as variations_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllVariationsEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        variations = variations_queries.get_all_variations(session)

        response_model = ResponseVariationDto(variations, many=True)
        response_model = response_model.dump()

        if len(variations) > 0:
            for variation in response_model:
                images = images_queries.get_images_for_variation(session, variation['id'])
                if len(images) > 0:
                    response_image = ResponseImageDto(images, many=True)
                    variation['images'] = response_image.dump()
                else:
                    variation['images'] = []

        session.close_session()

        return await self.make_response_json(status=200, body=response_model)
