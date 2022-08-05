from typing import List

from db.database import DBSession
from db.models.status_changes import DBStatusChanges


def create_status_changes(session: DBSession, order_id: int, status_id: int) -> DBStatusChanges:
    new_status_changes = DBStatusChanges(
        order_id=order_id,
        status_id=status_id
    )

    session.add_model(new_status_changes)

    return new_status_changes


def get_all_status_changes(session: DBSession, order_id: int) -> List[DBStatusChanges]:
    status_changes = session.get_all_status_changes_for_order(order_id)

    return status_changes
