from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.directory_item import ResponseCategoryDto
from db.database import DBSession
from db.queries import categories as categories_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllCategoriesEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        categories = categories_queries.get_all_categories(session)

        response_model = ResponseCategoryDto(categories, many=True)

        return await self.make_response_json(status=200, body=response_model.dump())
