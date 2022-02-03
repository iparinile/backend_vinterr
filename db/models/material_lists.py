from sqlalchemy import Column, Integer, ForeignKey

from db.models import BaseModel


class DBMaterialLists(BaseModel):
    __tablename__ = 'Material_lists'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    material_id = Column(Integer, ForeignKey('Categories.id', ondelete='CASCADE'), nullable=False)
