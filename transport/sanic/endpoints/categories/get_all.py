from sanic.request import Request
from sanic.response import BaseHTTPResponse
from transliterate import translit

from api.response.category import ResponseCategoryDto
from db.database import DBSession
from db.queries import categories as categories_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicInvalidRequestParameterException


class GetAllCategoriesEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        valid_request_params = ["parent_id", "name"]
        request_params = request.args
        for param_name in request_params.keys():
            if param_name == "name":
                request_params[param_name] = [translit(request_params[param_name][0], "ru")]
            if param_name not in valid_request_params:
                raise SanicInvalidRequestParameterException
        categories = categories_queries.get_all_categories(session, request_params)

        response_model = ResponseCategoryDto(categories, many=True)

        session.close_session()

        return await self.make_response_json(status=200, body=response_model.dump())
