from sqlalchemy import Column, Integer, ForeignKey

from db.models import BaseModel


class DBMaterialLists(BaseModel):
    __tablename__ = 'Material_lists'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    good_id = Column(Integer, ForeignKey('Goods.id', ondelete='CASCADE'), nullable=False)
    material_id = Column(Integer, ForeignKey('Materials.id', ondelete='CASCADE'), nullable=False)
