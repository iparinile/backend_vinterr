from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.create_directory_item import RequestCreateMaterialDto
from api.response.directory_item import ResponseCreateMaterialDto
from db.exceptions import DBMaterialExistsException, DBDataException, DBIntegrityException
from db.queries import materials as materials_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicMaterialConflictException, SanicDBException


class CreateMaterialEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateMaterialDto(body)

        try:
            db_material = materials_queries.create_material(session, request_model)
        except DBMaterialExistsException:
            raise SanicMaterialConflictException('Material with this name exists')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseCreateMaterialDto(db_material)

        return await self.make_response_json(body=response_model.dump(), status=201)
