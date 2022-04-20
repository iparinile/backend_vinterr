from typing import List

from api.request.create_directory_item import RequestCreateStatusDto
from db.database import DBSession
from db.exceptions import DBStatusExistsException, DBStatusNotExistsException
from db.models import DBStatuses


def create_status(session: DBSession, status: RequestCreateStatusDto) -> DBStatuses:
    new_status = DBStatuses(
        name=status.name
    )

    if session.get_status_by_name(new_status.name) is not None:
        raise DBStatusExistsException

    session.add_model(new_status)

    return new_status


def get_status(session: DBSession, status_id: int) -> DBStatuses:
    status = session.get_status_by_id(status_id)
    if status is None:
        raise DBStatusNotExistsException
    return status


def get_all_statuses(session: DBSession) -> List['DBStatuses']:
    statuses = session.get_all_statuses()
    return statuses


def patch_status(status: DBStatuses, new_name: str) -> DBStatuses:
    status.name = new_name
    return status


def delete_material(session: DBSession, material_id: int) -> None:
    session.delete_material(material_id)