import datetime

from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP

from db.models import BaseModel


class DBStatusChanges(BaseModel):
    __tablename__ = 'Status_changes'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    order_id = Column(Integer, ForeignKey('Orders.id', ondelete='SET NULL'), nullable=False)
    status_id = Column(Integer, ForeignKey('Statuses.id', ondelete='SET NULL'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.utcnow)
