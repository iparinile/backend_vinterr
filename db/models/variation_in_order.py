from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, BOOLEAN

from db.models import BaseModel


class DBVariationInOrder(BaseModel):
    __tablename__ = 'Variation_in_order'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    order_id = Column(Integer, ForeignKey('Orders.id', ondelete='CASCADE'), nullable=False)
    variation_id = Column(Integer, ForeignKey('Variations.id', ondelete='CASCADE'), nullable=False)
    amount = Column(Integer, nullable=False)
    current_price = Column(Integer, nullable=False)
