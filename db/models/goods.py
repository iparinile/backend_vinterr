from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from db.models import BaseModel


class DBGoods(BaseModel):
    __tablename__ = 'Goods'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    article = Column(VARCHAR(255), unique=True, nullable=False)
    good_1c_id = Column(Integer, unique=True)
    category_id = Column(Integer, ForeignKey('Categories.id', ondelete='CASCADE'), nullable=False)
    barcode = Column(Integer, unique=True, nullable=False)
    structure_id = Column(Integer, ForeignKey('Structure.id', ondelete='CASCADE'), nullable=False)
