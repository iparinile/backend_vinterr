from api.response.category import ResponseCategoryDto
from api.response.color import ResponseColorDto
from api.response.customer import ResponseCustomerDto
from api.response.directory_item import ResponseStatusDto, ResponseDeliveryTypeDto, ResponseSizeDto
from api.response.good import ResponseGoodDto
from api.response.order_from_db import ResponseOrderDBDto
from api.response.variation import ResponseVariationDto
from api.response.variation_in_order import ResponseVariationInOrderDto
from db.models import DBOrders, DBCustomers, DBStatuses, DBDeliveryTypes, DBVariationInOrders, DBVariations, DBColors, \
    DBSizes, DBGoods, DBCategories


def assembling_order_response(response_body: dict,
                              db_orders: DBOrders,
                              db_customers: DBCustomers,
                              db_statuses: DBStatuses,
                              db_delivery_types: DBDeliveryTypes,
                              db_variation_in_orders: DBVariationInOrders,
                              db_variations: DBVariations,
                              db_colors: DBColors,
                              db_sizes: DBSizes,
                              db_goods: DBGoods,
                              db_categories: DBCategories
                              ) -> dict:

    if db_orders.id not in response_body.keys():
        valid_order = ResponseOrderDBDto(db_orders).dump()
        valid_customer = ResponseCustomerDto(db_customers).dump()
        valid_status = ResponseStatusDto(db_statuses).dump()
        valid_delivery_type = ResponseDeliveryTypeDto(db_delivery_types).dump()

        valid_order['customer'] = valid_customer
        valid_order['status'] = valid_status
        valid_order['delivery_type'] = valid_delivery_type
        valid_order['variations'] = []
        response_body[valid_order['id']] = valid_order
    if db_variation_in_orders is not None:
        valid_good = ResponseGoodDto(db_goods).dump()
        valid_category = ResponseCategoryDto(db_categories).dump()
        valid_good['category'] = valid_category

        valid_variation = ResponseVariationDto(db_variations).dump()
        valid_color = ResponseColorDto(db_colors).dump()
        valid_size = ResponseSizeDto(db_sizes).dump()
        valid_variation_in_order = ResponseVariationInOrderDto(db_variation_in_orders).dump()
        valid_variation['good'] = valid_good
        valid_variation['color'] = valid_color
        valid_variation['size'] = valid_size
        valid_variation_in_order['variation'] = valid_variation
        response_body[db_orders.id]['variations'].append(valid_variation_in_order)

    return response_body
