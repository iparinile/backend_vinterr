from sqlalchemy import Column, VARCHAR, Integer, BOOLEAN, LargeBinary

from db.models import BaseModel


class DBUsers(BaseModel):
    __tablename__ = 'Users'

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    first_name = Column(VARCHAR(255), nullable=False)
    last_name = Column(VARCHAR(255), nullable=False)
    login = Column(VARCHAR(255), unique=True, nullable=False)
    password = Column(LargeBinary, nullable=False)
