from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.patch_directory_item import RequestPatchStatusDto
from api.response.directory_item import ResponseStatusDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBStatusNotExistsException
from db.queries import statuses as statuses_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicStatusNotFound


class StatusEndpoint(BaseEndpoint):

    async def method_patch(self, request: Request, body: dict, session: DBSession, status_id: int,
                           *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestPatchStatusDto(body)

        try:
            status = statuses_queries.get_status(session, status_id)
        except DBStatusNotExistsException:
            raise SanicStatusNotFound('Status not found')

        status = statuses_queries.patch_status(status, request_model.name)

        try:
            session.commit_session(need_close=True)
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseStatusDto(status)

        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_delete(self, request: Request, body: dict, session: DBSession, status_id: int,
                            *args, **kwargs) -> BaseHTTPResponse:

        try:
            status = statuses_queries.get_status(session, status_id)
        except DBStatusNotExistsException:
            raise SanicStatusNotFound('Status not found')

        statuses_queries.delete_status(session, status.id)

        try:
            session.commit_session(need_close=True)
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)

    async def method_get(self, request: Request, body: dict, session: DBSession, status_id: int,
                         *args, **kwargs) -> BaseHTTPResponse:

        try:
            status = statuses_queries.get_status(session, status_id)
        except DBStatusNotExistsException:
            raise SanicStatusNotFound('Status not found')

        response_model = ResponseStatusDto(status)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=200)
