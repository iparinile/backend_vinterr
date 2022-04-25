from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.create_directory_item import RequestCreateSizeDto
from api.response.directory_item import ResponseSizeDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBSizeExistsException
from db.queries import sizes as sizes_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicSizeConflictException


class CreateSizeEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateSizeDto(body)

        try:
            db_size = sizes_queries.create_size(session, request_model)
        except DBSizeExistsException:
            raise SanicSizeConflictException('Size with this name exists')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseSizeDto(db_size)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=201)
