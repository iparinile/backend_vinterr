from sanic.request import Request
from sanic.response import BaseHTTPResponse

from db.database import DBSession
from db.queries import orders as orders_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllOrdersEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        records = orders_queries.get_all_orders(session)

        response_body = dict()
        for db_orders, db_customers, db_statuses, db_deliveryTypes, db_variationInOrders in records:
            if db_orders.id not in response_body.keys():
                db_orders.customer = db_customers
                db_orders.status = db_statuses
                db_orders.delivery_type = db_deliveryTypes
                db_orders.variations = []
                response_body[db_orders.id] = db_orders
            response_body[db_orders.id].variations.append(db_variationInOrders)

        return await self.make_response_json(status=200, body=response_body)
