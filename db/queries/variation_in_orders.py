from api.request.create_order import VariationsInOrderDto
from db.database import DBSession
from db.models import DBVariationInOrders, DBOrders


def create_variation_in_order(
        session: DBSession,
        variation_in_order: dict,
        order: DBOrders
) -> DBVariationInOrders:
    new_variation_in_orders = DBVariationInOrders(
        order_id=order.id,
        variation_id=variation_in_order['variation_id'],
        amount=variation_in_order['amount'],
        current_price=variation_in_order['current_price']
    )

    session.add_model(new_variation_in_orders)

    return new_variation_in_orders
