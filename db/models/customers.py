from sqlalchemy import Column, VARCHAR, Integer, BOOLEAN, Date, LargeBinary

from db.models import BaseModel


class DBCustomers(BaseModel):
    __tablename__ = 'Customers'

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    first_name = Column(VARCHAR(255), nullable=False)
    second_name = Column(VARCHAR(255), nullable=False)
    last_name = Column(VARCHAR(255), nullable=False)
    login = Column(VARCHAR(255), unique=True)
    password = Column(LargeBinary)
    email = Column(VARCHAR(255), unique=False)
    birthday = Column(Date)
    phone_number = Column(VARCHAR(18), unique=False, nullable=False)
    is_registered = Column(BOOLEAN, default=False)
