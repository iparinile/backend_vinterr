from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.patch_order import RequestPatchOrderDto
from api.response.order import ResponseOrderDto
from api.response.order_from_db import ResponseOrderDBDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBOrderNotExistsException
from db.queries import orders as orders_queries
from helpers.psycopg2_exceptions.get_details import get_details_psycopg2_exception
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.endpoints.orders.helpers_def import assembling_order_response
from transport.sanic.exceptions import SanicDBException, SanicDBUniqueFieldException, SanicOrderNotFound


class OrderEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, order_id: int,
                         *args, **kwargs) -> BaseHTTPResponse:
        db_orders, db_customers, db_statuses, db_delivery_types, db_variation_in_orders, db_variations, db_colors, \
        db_sizes, db_goods, db_categories = orders_queries.get_order(session, order_id)
        response_body = dict()

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

        response_body = response_body[order_id]

        session.close_session()

        return await self.make_response_json(status=200, body=response_body)

    async def method_patch(self, request: Request, body: dict, session: DBSession, order_id: int,
                           *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestPatchOrderDto(body)

        try:
            order = orders_queries.get_order_by_id(session, order_id)
        except DBOrderNotExistsException:
            raise SanicOrderNotFound('Order not found')

        order = orders_queries.patch_order(order, request_model)

        try:
            session.commit_session()
        except DBDataException as e:
            raise SanicDBException(str(e))
        except DBIntegrityException as e:
            exception_code, exception_info = get_details_psycopg2_exception(e)
            if exception_code in ['23503', '23505']:
                raise SanicDBUniqueFieldException(exception_info)
            else:
                raise SanicDBException(str(e))

        response_model = ResponseOrderDBDto(order)

        session.close_session()
        return await self.make_response_json(body=response_model.dump(), status=200)
