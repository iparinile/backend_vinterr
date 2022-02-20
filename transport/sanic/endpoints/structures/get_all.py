from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.directory_item import ResponseStructureDto
from db.database import DBSession
from db.queries import structures as structures_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllStructuresEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        structures = structures_queries.get_all_structures(session)

        response_model = ResponseStructureDto(structures, many=True)

        return await self.make_response_json(status=200, body=response_model.dump())
