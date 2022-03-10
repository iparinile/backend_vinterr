from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, BOOLEAN

from db.models import BaseModel


class DBVariations(BaseModel):
    __tablename__ = 'Variations'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    good_id = Column(Integer, ForeignKey('Goods.id', ondelete='CASCADE'), nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    color_id = Column(Integer, ForeignKey('Colors.id', ondelete='CASCADE'), nullable=False)
    size_id = Column(Integer, ForeignKey('Sizes.id', ondelete='CASCADE'), nullable=False)
    price = Column(Integer, nullable=False)
    discounted_price = Column(Integer)
    variation_1c_id = Column(VARCHAR(255), unique=True)
    amount = Column(Integer)
    barcode = Column(VARCHAR(255))
    is_sale = Column(BOOLEAN(), default=False)
    is_new = Column(BOOLEAN(), default=False)
