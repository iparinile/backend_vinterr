from typing import List

from api.request.create_category import RequestCreateCategoryDto
from db.database import DBSession
from db.exceptions import DBCategoryExistsException, DBCategoryNotExistsException
from db.models import DBCategories


def create_category(session: DBSession, category: RequestCreateCategoryDto) -> DBCategories:
    new_category = DBCategories(
        name=category.name,
        parent_id=category.parent_id
    )

    if session.get_category_by_name(new_category.name) is not None:
        raise DBCategoryExistsException

    session.add_model(new_category)

    return new_category


def get_all_categories(session: DBSession) -> List['DBCategories']:
    categories = session.get_all_categories()
    return categories


def get_category(session: DBSession, category_id: int) -> DBCategories:
    category = session.get_category_by_id(category_id)
    if category is None:
        raise DBCategoryNotExistsException
    return category


def patch_category(category: DBCategories, new_name: str) -> DBCategories:
    category.name = new_name
    return category


def delete_category(session: DBSession, category_id: int) -> None:
    session.delete_category(category_id)
