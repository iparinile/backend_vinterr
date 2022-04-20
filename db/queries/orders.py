from typing import List

from api.request.create_order import RequestCreateOrderDto
from api.request.patch_order import RequestPatchOrderDto
from db.database import DBSession
from db.exceptions import DBOrderNotExistsException, DBOrderExistsException
from db.models import DBOrders, DBCustomers


def create_order(
        session: DBSession,
        body_request: RequestCreateOrderDto,
        customer: DBCustomers
) -> DBOrders:
    new_order = DBOrders(
        customer_id=customer.id,
        status_id=body_request.status_id,
        delivery_type_id=body_request.delivery_type_id,
        delivery_address=body_request.delivery_address,
        delivery_cost=body_request.delivery_cost
    )

    session.add_model(new_order)

    return new_order


def get_all_orders(session: DBSession) -> List['DBOrders']:
    records = session.get_all_orders()
    return records


def get_order(session: DBSession, order_id: int) -> tuple:
    order = session.get_order(order_id)

    if order is None:
        raise DBOrderNotExistsException

    return order


def get_order_by_sberbank_id(session: DBSession, sberbank_order_id: str) -> tuple:
    order = session.get_order_by_sberbank_id(sberbank_order_id)

    if order is None:
        raise DBOrderNotExistsException

    return order


def patch_order(order: DBOrders, patch_fields_order: RequestPatchOrderDto) -> DBOrders:
    for attr in patch_fields_order.fields:
        if hasattr(patch_fields_order, attr):
            value = getattr(patch_fields_order, attr)
            setattr(order, attr, value)
    return order


def patch_sberbank_id(session: DBSession, order: DBOrders, sberbank_id: str) -> DBOrders:
    db_order = session.get_order_by_sberbank_id(sberbank_id)
    if db_order is not None:
        raise DBOrderExistsException

    order.sberbank_id = sberbank_id

    return order
