import datetime

from sqlalchemy import Column, Integer, ForeignKey, BOOLEAN, TIMESTAMP, VARCHAR, FLOAT

from db.models import BaseModel


class DBOrders(BaseModel):
    __tablename__ = 'Orders'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    sberbank_id = Column(VARCHAR())
    customer_id = Column(Integer, ForeignKey('Customers.id', ondelete='CASCADE'), nullable=False)
    status_id = Column(Integer, ForeignKey('Statuses.id', ondelete='CASCADE'), nullable=False)
    delivery_type_id = Column(Integer, ForeignKey('Delivery_types.id', ondelete='CASCADE'), nullable=False)
    is_payed = Column(BOOLEAN(), default=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.utcnow)
    delivery_address = Column(VARCHAR())
    delivery_cost = Column(FLOAT)
