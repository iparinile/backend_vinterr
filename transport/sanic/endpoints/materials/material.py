from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.patch_directory_item import RequestPatchMaterialDto
from api.response.directory_item import ResponseMaterialDto
from db.database import DBSession
from db.exceptions import DBMaterialNotExistsException, DBDataException, DBIntegrityException
from db.queries import materials as materials_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicMaterialNotFound, SanicDBException


class MaterialEndpoint(BaseEndpoint):

    async def method_patch(self, request: Request, body: dict, session: DBSession, material_id: int,
                           *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestPatchMaterialDto(body)

        try:
            material = materials_queries.get_material(session, material_id)
        except DBMaterialNotExistsException:
            raise SanicMaterialNotFound('Material not found')

        material = materials_queries.patch_material(material, request_model.name)

        try:
            session.commit_session(need_close=True)
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseMaterialDto(material)

        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_delete(self, request: Request, body: dict, session: DBSession, material_id: int,
                            *args, **kwargs) -> BaseHTTPResponse:

        try:
            material = materials_queries.get_material(session, material_id)
        except DBMaterialNotExistsException:
            raise SanicMaterialNotFound('Material not found')

        materials_queries.delete_material(session, material.id)

        try:
            session.commit_session(need_close=True)
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)

    async def method_get(self, request: Request, body: dict, session: DBSession, material_id: int,
                         *args, **kwargs) -> BaseHTTPResponse:

        try:
            material = materials_queries.get_material(session, material_id)
        except DBMaterialNotExistsException:
            raise SanicMaterialNotFound('Material not found')

        response_model = ResponseMaterialDto(material)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=200)
