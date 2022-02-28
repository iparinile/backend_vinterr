from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.patch_category import RequestPatchCategoryDto
from api.response.category import ResponseCategoryDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBCategoryNotExistsException
from db.queries import categories as categories_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicCategoryNotFound


class CategoryEndpoint(BaseEndpoint):

    async def method_patch(self, request: Request, body: dict, session: DBSession, category_id: int,
                           *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestPatchCategoryDto(body)

        try:
            category = categories_queries.get_category(session, category_id)
        except DBCategoryNotExistsException:
            raise SanicCategoryNotFound('Category not found')

        category = categories_queries.patch_category(category, request_model.name)

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseCategoryDto(category)

        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_delete(self, request: Request, body: dict, session: DBSession, category_id: int,
                            *args, **kwargs) -> BaseHTTPResponse:

        try:
            category = categories_queries.get_category(session, category_id)
        except DBCategoryNotExistsException:
            raise SanicCategoryNotFound('Category not found')

        categories_queries.delete_category(session, category.id)

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)

    async def method_get(self, request: Request, body: dict, session: DBSession, category_id: int,
                         *args, **kwargs) -> BaseHTTPResponse:

        try:
            category = categories_queries.get_category(session, category_id)
        except DBCategoryNotExistsException:
            raise SanicCategoryNotFound('Category not found')

        response_model = ResponseCategoryDto(category)

        return await self.make_response_json(body=response_model.dump(), status=200)
