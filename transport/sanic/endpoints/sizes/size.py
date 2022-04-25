from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.patch_directory_item import RequestPatchSizeDto
from api.response.directory_item import ResponseSizeDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBSizeNotExistsException
from db.queries import sizes as sizes_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicSizeNotFound


class SizeEndpoint(BaseEndpoint):

    async def method_patch(self, request: Request, body: dict, session: DBSession, size_id: int,
                           *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestPatchSizeDto(body)

        try:
            size = sizes_queries.get_size(session, size_id)
        except DBSizeNotExistsException:
            raise SanicSizeNotFound('Size not found')

        size = sizes_queries.patch_size(size, request_model.name)

        try:
            session.commit_session(need_close=True)
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseSizeDto(size)

        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_delete(self, request: Request, body: dict, session: DBSession, size_id: int,
                            *args, **kwargs) -> BaseHTTPResponse:

        try:
            size = sizes_queries.get_size(session, size_id)
        except DBSizeNotExistsException:
            raise SanicSizeNotFound('Size not found')

        sizes_queries.delete_size(session, size.id)

        try:
            session.commit_session(need_close=True)
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)

    async def method_get(self, request: Request, body: dict, session: DBSession, size_id: int,
                         *args, **kwargs) -> BaseHTTPResponse:

        try:
            size = sizes_queries.get_size(session, size_id)
        except DBSizeNotExistsException:
            raise SanicSizeNotFound('Size not found')

        response_model = ResponseSizeDto(size)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=200)
