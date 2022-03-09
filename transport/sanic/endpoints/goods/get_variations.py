from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.variation import ResponseVariationDto
from db.database import DBSession
from db.exceptions import DBVariationsForGoodNotExistsException
from db.queries import variations as variations_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicVariationsForGoodNotFound


class GetVariationsForGoodEndpoint(BaseEndpoint):
    async def method_get(
            self,
            request: Request,
            body: dict,
            session: DBSession,
            good_id: int,
            *args, **kwargs
    ) -> BaseHTTPResponse:
        try:
            variations = variations_queries.get_variations_for_good(session, good_id)
        except DBVariationsForGoodNotExistsException:
            raise SanicVariationsForGoodNotFound("Variations for good not found")

        response_model = ResponseVariationDto(variations, many=True)

        return await self.make_response_json(status=200, body=response_model.dump())
