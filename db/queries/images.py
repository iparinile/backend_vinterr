from typing import List

from db.database import DBSession
from db.models import DBImages


def get_images_for_variation(session: DBSession, variation_id: int) -> List['DBImages']:
    images = session.get_images_by_variation_id(variation_id)
    return images
