from typing import List

from api.request.create_directory_item import RequestCreateSizeDto
from db.database import DBSession
from db.exceptions import DBSizeExistsException, DBSizeNotExistsException
from db.models import DBSizes


def create_size(session: DBSession, size: RequestCreateSizeDto) -> DBSizes:
    new_size = DBSizes(
        name=size.name
    )

    if session.get_size_by_name(new_size.name) is not None:
        raise DBSizeExistsException

    session.add_model(new_size)

    return new_size


def get_all_sizes(session: DBSession) -> List['DBSizes']:
    sizes = session.get_all_sizes()
    return sizes


def get_size(session: DBSession, size_id: int) -> DBSizes:
    size = session.get_size_by_id(size_id)
    if size is None:
        raise DBSizeNotExistsException
    return size


def patch_size(size: DBSizes, new_name: str) -> DBSizes:
    size.name = new_name
    return size


def delete_size(session: DBSession, size_id: int) -> None:
    session.delete_size(size_id)
