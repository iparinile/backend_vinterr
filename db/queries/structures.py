from typing import List

from api.request.create_directory_item import RequestCreateStructureDto
from db.database import DBSession
from db.exceptions import DBStructureExistsException, DBStructureNotExistsException
from db.models import DBCategories, DBStructures


def create_structure(session: DBSession, structure: RequestCreateStructureDto) -> DBStructures:
    new_structure = DBStructures(
        name=structure.name
    )

    if session.get_structure_by_name(new_structure.name) is not None:
        raise DBStructureExistsException

    session.add_model(new_structure)

    return new_structure


def get_all_structures(session: DBSession) -> List['DBStructures']:
    structures = session.get_all_structures()
    return structures


def get_structure(session: DBSession, structure_id: int) -> DBStructures:
    structure = session.get_structure_by_id(structure_id)
    if structure is None:
        raise DBStructureNotExistsException
    return structure


def patch_structure(structure: DBStructures, new_name: str) -> DBStructures:
    structure.name = new_name
    return structure


def delete_structure(session: DBSession, structure_id: int) -> None:
    session.delete_structure(structure_id)
