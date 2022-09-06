from sanic import Request
from sanic.response import BaseHTTPResponse

from api.request.patch_directory_item import RequestPatchProductsCareDto
from api.response.directory_item import ResponseProductsCareDto
from db.database import DBSession
from db.exceptions import DBProductsCareNotExistsException, DBDataException, DBIntegrityException
from db.queries import products_care as products_care_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicProductsCareNotFound, SanicDBException


class ProductsCareEndpoint(BaseEndpoint):

    async def method_patch(self, request: Request, body: dict, session: DBSession, products_care_id: int,
                           *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestPatchProductsCareDto(body)

        try:
            products_care = products_care_queries.get_products_care(session, products_care_id)
        except DBProductsCareNotExistsException:
            raise SanicProductsCareNotFound('Products care not found')

        products_care = products_care_queries.patch_products_care(products_care, request_model.name)

        response_model = ResponseProductsCareDto(products_care)

        try:
            session.commit_session(need_close=True)
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_delete(self, request: Request, body: dict, session: DBSession, products_care_id: int,
                            *args, **kwargs) -> BaseHTTPResponse:

        try:
            products_care = products_care_queries.get_products_care(session, products_care_id)
        except DBProductsCareNotExistsException:
            raise SanicProductsCareNotFound('Products care not found')

        products_care_queries.delete_products_care(session, products_care.id)

        try:
            session.commit_session(need_close=True)
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)

    async def method_get(self, request: Request, body: dict, session: DBSession, products_care_id: int,
                         *args, **kwargs) -> BaseHTTPResponse:

        try:
            products_care = products_care_queries.get_products_care(session, products_care_id)
        except DBProductsCareNotExistsException:
            raise SanicProductsCareNotFound('Structure not found')

        response_model = ResponseProductsCareDto(products_care)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=200)
