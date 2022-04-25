from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.patch_color import RequestPatchColorDto
from api.response.color import ResponseColorDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBColorNotExistsException
from db.queries import colors as colors_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicColorNotFound


class ColorEndpoint(BaseEndpoint):

    async def method_patch(self, request: Request, body: dict, session: DBSession, color_id: int,
                           *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestPatchColorDto(body)

        try:
            color = colors_queries.get_color(session, color_id)
        except DBColorNotExistsException:
            raise SanicColorNotFound('Color not found')

        color = colors_queries.patch_color(color, request_model)

        try:
            session.commit_session(need_close=True)
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseColorDto(color)

        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_delete(self, request: Request, body: dict, session: DBSession, color_id: int,
                            *args, **kwargs) -> BaseHTTPResponse:

        try:
            color = colors_queries.get_color(session, color_id)
        except DBColorNotExistsException:
            raise SanicColorNotFound('Color not found')

        colors_queries.delete_color(session, color.id)

        try:
            session.commit_session(need_close=True)
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)

    async def method_get(self, request: Request, body: dict, session: DBSession, color_id: int,
                         *args, **kwargs) -> BaseHTTPResponse:

        try:
            color = colors_queries.get_color(session, color_id)
        except DBColorNotExistsException:
            raise SanicColorNotFound('Color not found')

        response_model = ResponseColorDto(color)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=200)
