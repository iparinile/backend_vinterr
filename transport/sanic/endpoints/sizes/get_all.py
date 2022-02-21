from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.directory_item import ResponseSizeDto
from db.database import DBSession
from db.queries import sizes as sizes_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllSizesEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        sizes = sizes_queries.get_all_sizes(session)

        response_model = ResponseSizeDto(sizes, many=True)

        return await self.make_response_json(status=200, body=response_model.dump())
