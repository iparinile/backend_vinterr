from api.request.create_directory_item import RequestCreateMaterialDto
from db.database import DBSession
from db.exceptions import DBMaterialExistsException
from db.models import DBMaterials


def create_material(session: DBSession, material: RequestCreateMaterialDto) -> DBMaterials:
    new_material = DBMaterials(
        name=material.name
    )

    if session.get_material_by_name(new_material.name) is not None:
        raise DBMaterialExistsException

    session.add_model(new_material)

    return new_material
