from sqlalchemy import Column, VARCHAR, Integer, VARBINARY, BOOLEAN

from db.models import BaseModel


class DBUsers(BaseModel):
    __tablename__ = 'Users'

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    first_name = Column(VARCHAR(255), nullable=False)
    last_name = Column(VARCHAR(255), nullable=False)
    login = Column(VARCHAR(255), unique=True, nullable=False)
    password = Column(VARBINARY(), nullable=False)
    group_id = Column(Integer)
    is_delete = Column(BOOLEAN())
