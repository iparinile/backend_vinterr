import datetime

from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, BOOLEAN, TIMESTAMP

from db.models import BaseModel


class DBOrders(BaseModel):
    __tablename__ = 'Orders'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    customer_id = Column(Integer, ForeignKey('Customers.id', ondelete='CASCADE'), nullable=False)
    status_id = Column(Integer, ForeignKey('Statuses.id', ondelete='CASCADE'), nullable=False)
    delivery_type_id = Column(Integer, ForeignKey('Delivery_types.id', ondelete='CASCADE'), nullable=False)
    is_payed = Column(BOOLEAN(), default=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.utcnow)
