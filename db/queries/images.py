from typing import List

from db.database import DBSession
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
