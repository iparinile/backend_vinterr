from api.request.create_directory_item import RequestCreateMaterialDto
from db.database import DBSession
from db.exceptions import DBMaterialExistsException, DBMaterialNotExistsException
from db.models import DBMaterials


def create_material(session: DBSession, material: RequestCreateMaterialDto) -> DBMaterials:
    new_material = DBMaterials(
        name=material.name
    )

    if session.get_material_by_name(new_material.name) is not None:
        raise DBMaterialExistsException

    session.add_model(new_material)

    return new_material


def get_material(session: DBSession, material_id: int) -> DBMaterials:
    material = session.get_material_by_id(material_id)
    if material is None:
        raise DBMaterialNotExistsException
    return material


def patch_material(material: DBMaterials, new_name: str) -> DBMaterials:
    material.name = new_name
    return material


def delete_material(session: DBSession, material_id: int) -> None:
    session.delete_material(material_id)
