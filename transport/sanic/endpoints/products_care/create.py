from sanic.response import Request, BaseHTTPResponse

from api.request.create_directory_item import RequestCreateProductsCareDto
from api.response.directory_item import ResponseProductsCareDto
from db.database import DBSession
from db.exceptions import DBProductsCareExistsException, DBDataException, DBIntegrityException
from db.queries import products_care as products_care_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicProductsCareConflictException, SanicDBException


class CreateProductsCareEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateProductsCareDto(body)

        try:
            db_products_care = products_care_queries.create_products_care(session, request_model)
        except DBProductsCareExistsException:
            raise SanicProductsCareConflictException('Products care with this name exists')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseProductsCareDto(db_products_care)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=201)
