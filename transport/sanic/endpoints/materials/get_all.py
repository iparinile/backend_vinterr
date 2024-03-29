from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.directory_item import ResponseMaterialDto
from db.database import DBSession
from db.queries import materials as materials_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllMaterialsEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        materials = materials_queries.get_all_materials(session)

        response_model = ResponseMaterialDto(materials, many=True)

        session.close_session()

        return await self.make_response_json(status=200, body=response_model.dump())
