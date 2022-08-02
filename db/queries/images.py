from typing import List

from db.database import DBSession
from db.exceptions import DBImageNotExistsException
from db.models import DBImages


def get_images_for_variation(session: DBSession, variation_id: int) -> List['DBImages']:
    images = session.get_images_by_variation_id(variation_id)
    return images


def create_image(session: DBSession, variation_id: int, image_path: str) -> DBImages:
    db_image = DBImages(
        url=image_path,
        variation_id=variation_id
    )
    session.add_model(db_image)
    return db_image


def get_image_by_url(session: DBSession, image_url: str) -> DBImages:
    db_image = session.get_images_by_url(image_url)
    if db_image is None:
        raise DBImageNotExistsException

    return db_image
