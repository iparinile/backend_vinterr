from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.directory_item import ResponseProductsCareDto
from db.database import DBSession
from db.queries import products_care as products_care_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllProductsCareEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        products_care = products_care_queries.get_all_products_care(session)

        response_model = ResponseProductsCareDto(products_care, many=True)

        session.close_session()

        return await self.make_response_json(status=200, body=response_model.dump())
