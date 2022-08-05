from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.status_changes import ResponseStatusChangesDto
from db.database import DBSession
from db.queries import status_changes as status_changes_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllStatusChangesEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, order_id: int,
                         *args, **kwargs) -> BaseHTTPResponse:
        status_changes = status_changes_queries.get_all_status_changes(session, order_id)

        response_model = ResponseStatusChangesDto(status_changes, many=True)

        session.close_session()

        return await self.make_response_json(status=200, body=response_model.dump())
