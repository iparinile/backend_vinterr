from sanic.request import Request
from sanic.response import BaseHTTPResponse

from db.database import DBSession
from db.queries import orders as orders_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.endpoints.orders.helpers_def import assembling_order_response


class GetAllOrdersEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        records = orders_queries.get_all_orders(session)
        response_body = dict()

        for db_orders, db_customers, db_statuses, db_delivery_types, db_variation_in_orders, db_variations, db_colors, \
            db_sizes, db_goods, db_categories in records:
            response_body = assembling_order_response(response_body,
                                                      db_orders,
                                                      db_customers,
                                                      db_statuses,
                                                      db_delivery_types,
                                                      db_variation_in_orders,
                                                      db_variations,
                                                      db_colors,
                                                      db_sizes,
                                                      db_goods,
                                                      db_categories
                                                      )

        response_body = [order for order in response_body.values()]

        session.close_session()

        return await self.make_response_json(status=200, body=response_body)
