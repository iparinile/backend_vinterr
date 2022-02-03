from sqlalchemy import Column, Integer, VARCHAR

from db.models import BaseModel


class DBStructure(BaseModel):
    __tablename__ = 'Structure'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    value = Column(VARCHAR(255), unique=True, nullable=False)
