from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.variation import ResponseCreateVariationDto
from db.database import DBSession
from db.queries import variations as variations_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllVariationsEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        variations = variations_queries.get_all_variations(session)

        response_model = ResponseCreateVariationDto(variations, many=True)

        return await self.make_response_json(status=200, body=response_model.dump())
