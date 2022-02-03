from sqlalchemy import Column, VARCHAR, Integer, VARBINARY, BOOLEAN, Date

from db.models import BaseModel


class DBCustomers(BaseModel):
    __tablename__ = 'Customers'

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    first_name = Column(VARCHAR(255), nullable=False)
    last_name = Column(VARCHAR(255), nullable=False)
    login = Column(VARCHAR(255), unique=True)
    password = Column(VARBINARY())
    email = Column(VARCHAR(255), unique=True)
    birthday = Column(Date)
    phone_number = Column(VARCHAR(10), unique=True)
    is_registered = Column(BOOLEAN, default=False)
