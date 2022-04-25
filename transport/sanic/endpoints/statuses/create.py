from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.create_directory_item import RequestCreateStatusDto
from api.response.directory_item import ResponseStatusDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBStatusExistsException
from db.queries import statuses as statuses_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicStatusConflictException


class CreateStatusEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateStatusDto(body)

        try:
            db_status = statuses_queries.create_status(session, request_model)
        except DBStatusExistsException:
            raise SanicStatusConflictException('Status with this name exists')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseStatusDto(db_status)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=201)
