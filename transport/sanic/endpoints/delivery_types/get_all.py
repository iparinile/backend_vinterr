from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.directory_item import ResponseDeliveryTypeDto
from db.database import DBSession
from db.queries import delivery_types as delivery_types_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllDeliveryTypesEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        delivery_types = delivery_types_queries.get_all_delivery_types(session)

        response_model = ResponseDeliveryTypeDto(delivery_types, many=True)

        return await self.make_response_json(status=200, body=response_model.dump())
