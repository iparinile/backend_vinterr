from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.color import ResponseColorDto
from db.database import DBSession
from db.queries import colors as colors_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllColorsEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        colors = colors_queries.get_all_colors(session)

        response_model = ResponseColorDto(colors, many=True)

        session.close_session()

        return await self.make_response_json(status=200, body=response_model.dump())
