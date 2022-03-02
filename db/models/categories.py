from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from db.models import BaseModel


class DBCategories(BaseModel):
    __tablename__ = 'Categories'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    parent_id = Column(Integer, ForeignKey('Categories.id', ondelete='SET NULL'), nullable=True)
