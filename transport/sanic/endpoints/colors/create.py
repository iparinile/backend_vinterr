from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.create_color import RequestCreateColorDto
from api.response.color import ResponseColorDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBColorNameExistsException, DBColorCodeExistsException
from db.queries import colors as colors_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicColorConflictException


class CreateColorEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateColorDto(body)

        try:
            db_color = colors_queries.create_color(session, request_model)
        except DBColorNameExistsException:
            raise SanicColorConflictException('Color with this name exists')
        except DBColorCodeExistsException:
            raise SanicColorConflictException('Color with this code exists')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseColorDto(db_color)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=201)
