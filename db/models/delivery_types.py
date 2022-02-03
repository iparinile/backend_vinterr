from sqlalchemy import Column, Integer, VARCHAR

from db.models import BaseModel


class DBDeliveryTypes(BaseModel):
    __tablename__ = 'Delivery_types'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(VARCHAR(255), unique=True, nullable=False)
