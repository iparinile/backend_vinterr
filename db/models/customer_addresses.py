from sqlalchemy import Column, VARCHAR, Integer, VARBINARY, Date, ForeignKey

from db.models import BaseModel


class DBCustomerAddresses(BaseModel):
    __tablename__ = 'Customer_addresses'

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    customer_id = Column(Integer, ForeignKey('Customers.id', ondelete='CASCADE'), nullable=False)
    city_id = Column(Integer, ForeignKey('Cities.id', ondelete='CASCADE'), nullable=False)
    streets_id = Column(Integer, ForeignKey('Streets.id', ondelete='CASCADE'), nullable=False)
    house_number = Column(VARCHAR(10), nullable=False)
    apartment = Column(Integer, nullable=False)
    other_info = Column(VARCHAR(255))
