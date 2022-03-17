from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.category import ResponseCategoryDto
from api.response.color import ResponseColorDto
from api.response.customer import ResponseCustomerDto
from api.response.directory_item import ResponseStatusDto, ResponseDeliveryTypeDto, ResponseSizeDto
from api.response.good import ResponseGoodDto
from api.response.order_from_db import ResponseOrderDBDto
from api.response.variation import ResponseVariationDto
from api.response.variation_in_order import ResponseVariationInOrderDto
from db.database import DBSession
from db.queries import orders as orders_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllOrdersEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        records = orders_queries.get_all_orders(session)

        response_body = dict()
        for db_orders, db_customers, db_statuses, db_deliveryTypes, db_variationInOrders, db_variations, db_colors, \
            db_sizes, db_goods, db_categories in records:
            if db_orders.id not in response_body.keys():
                valid_order = ResponseOrderDBDto(db_orders).dump()
                valid_customer = ResponseCustomerDto(db_customers).dump()
                valid_status = ResponseStatusDto(db_statuses).dump()
                valid_delivery_type = ResponseDeliveryTypeDto(db_deliveryTypes).dump()

                valid_order['customer'] = valid_customer
                valid_order['status'] = valid_status
                valid_order['delivery_type'] = valid_delivery_type
                valid_order['variations'] = []
                response_body[valid_order['id']] = valid_order
            if db_variationInOrders is not None:
                valid_good = ResponseGoodDto(db_goods).dump()
                valid_category = ResponseCategoryDto(db_categories).dump()
                valid_good['category'] = valid_category

                valid_variation = ResponseVariationDto(db_variations).dump()
                valid_color = ResponseColorDto(db_colors).dump()
                valid_size = ResponseSizeDto(db_sizes).dump()
                valid_variation_in_order = ResponseVariationInOrderDto(db_variationInOrders).dump()
                valid_variation['good'] = valid_good
                valid_variation['color'] = valid_color
                valid_variation['size'] = valid_size
                valid_variation_in_order['variation'] = valid_variation
                response_body[db_orders.id]['variations'].append(valid_variation_in_order)

        return await self.make_response_json(status=200, body=response_body)
