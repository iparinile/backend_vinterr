from typing import List

from api.request.create_order import RequestCreateOrderDto
from db.database import DBSession
from db.models import DBOrders, DBCustomers


def create_order(
        session: DBSession,
        body_request: RequestCreateOrderDto,
        customer: DBCustomers
) -> DBOrders:
    new_order = DBOrders(
        customer_id=customer.id,
        status_id=body_request.status_id,
        delivery_type_id=body_request.delivery_type_id
    )

    session.add_model(new_order)

    return new_order


def get_all_orders(session: DBSession) -> List['DBOrders']:
    records = session.get_all_orders()
    return records
