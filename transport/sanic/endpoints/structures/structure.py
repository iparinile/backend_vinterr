from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.patch_directory_item import RequestPatchStructureDto
from api.response.directory_item import ResponseStructureDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBStructureNotExistsException
from db.queries import structures as structures_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicStructureNotFound


class StructureEndpoint(BaseEndpoint):

    async def method_patch(self, request: Request, body: dict, session: DBSession, structure_id: int,
                           *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestPatchStructureDto(body)

        try:
            structure = structures_queries.get_structure(session, structure_id)
        except DBStructureNotExistsException:
            raise SanicStructureNotFound('Structure not found')

        structure = structures_queries.patch_structure(structure, request_model.name)

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseStructureDto(structure)

        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_delete(self, request: Request, body: dict, session: DBSession, structure_id: int,
                            *args, **kwargs) -> BaseHTTPResponse:

        try:
            structure = structures_queries.get_structure(session, structure_id)
        except DBStructureNotExistsException:
            raise SanicStructureNotFound('Structure not found')

        structures_queries.delete_structure(session, structure.id)

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)

    async def method_get(self, request: Request, body: dict, session: DBSession, structure_id: int,
                         *args, **kwargs) -> BaseHTTPResponse:

        try:
            structure = structures_queries.get_structure(session, structure_id)
        except DBStructureNotExistsException:
            raise SanicStructureNotFound('Structure not found')

        response_model = ResponseStructureDto(structure)

        return await self.make_response_json(body=response_model.dump(), status=200)
