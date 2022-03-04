from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, BOOLEAN

from db.models import BaseModel


class DBGoods(BaseModel):
    __tablename__ = 'Goods'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    article = Column(VARCHAR(255), unique=True, nullable=False)
    good_1c_id = Column(VARCHAR(255), unique=True)
    category_id = Column(Integer, ForeignKey('Categories.id', ondelete='CASCADE'), nullable=False)
    barcode = Column(VARCHAR(255))
    structure_id = Column(Integer, ForeignKey('Structures.id', ondelete='CASCADE'), nullable=False)
    description = Column(VARCHAR(), nullable=False)
    default_variation = Column(Integer, ForeignKey('Variations.id', ondelete='SET NULL'))
    is_visible = Column(BOOLEAN(), default=True)
