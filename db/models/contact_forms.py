from sqlalchemy import Column, Integer, VARCHAR

from db.models import BaseModel


class DBContactForms(BaseModel):
    __tablename__ = 'Contact_forms'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    customer_name = Column(VARCHAR(255), unique=False, nullable=False)
    phone_number = Column(VARCHAR(255), unique=False, nullable=False)
    text = Column(VARCHAR(255), default=None)
    email = Column(VARCHAR(255), default=None)
