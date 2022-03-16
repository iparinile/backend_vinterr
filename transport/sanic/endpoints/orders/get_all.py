from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.directory_item import ResponseMaterialDto
from db.database import DBSession
from db.queries import orders as orders_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllOrdersEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        records = orders_queries.get_all_orders(session)

        for db_orders, db_customers, db_statuses, db_deliveryTypes, db_variationInOrders in records:


        return await self.make_response_json(status=200, body=response_model.dump())
