from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.directory_item import ResponseStatusDto
from db.database import DBSession
from db.queries import statuses as statuses_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllStatusesEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        statuses = statuses_queries.get_all_statuses(session)

        response_model = ResponseStatusDto(statuses, many=True)

        return await self.make_response_json(status=200, body=response_model.dump())
