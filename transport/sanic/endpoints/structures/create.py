from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.create_directory_item import RequestCreateStructureDto
from api.response.directory_item import ResponseStructureDto
from db.exceptions import DBDataException, DBIntegrityException, DBStructureExistsException
from db.queries import structures as structures_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicStructureConflictException


class CreateStructureEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateStructureDto(body)

        try:
            db_structure = structures_queries.create_structure(session, request_model)
        except DBStructureExistsException:
            raise SanicStructureConflictException('Structure with this name exists')

        try:
            session.commit_session(need_close=True)
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseStructureDto(db_structure)

        return await self.make_response_json(body=response_model.dump(), status=201)
