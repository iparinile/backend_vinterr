from typing import List

from api.request.create_color import RequestCreateColorDto
from api.request.patch_color import RequestPatchColorDto
from db.database import DBSession
from db.exceptions import DBColorNameExistsException, DBColorNotExistsException
from db.models import DBColors


def create_color(session: DBSession, color: RequestCreateColorDto) -> DBColors:
    new_color = DBColors(
        name=color.name,
        code=color.code
    )

    if session.get_color_by_name(new_color.name) is not None:
        raise DBColorNameExistsException

    session.add_model(new_color)

    return new_color


def get_color(session: DBSession, color_id: int) -> DBColors:
    color = session.get_color_by_id(color_id)
    if color is None:
        raise DBColorNotExistsException
    return color


def get_all_colors(session: DBSession) -> List['DBColors']:
    colors = session.get_all_colors()
    return colors


def patch_color(color: DBColors, patch_fields_color: RequestPatchColorDto) -> DBColors:
    for attr in patch_fields_color.fields:
        if hasattr(patch_fields_color, attr):
            value = getattr(patch_fields_color, attr)
            setattr(color, attr, value)
    return color


def delete_color(session: DBSession, color_id: int) -> None:
    session.delete_color(color_id)
