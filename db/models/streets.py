from sqlalchemy import Column, Integer, VARCHAR

from db.models import BaseModel


class DBStreets(BaseModel):
    __tablename__ = 'Streets'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(VARCHAR(255), unique=True, nullable=False)
