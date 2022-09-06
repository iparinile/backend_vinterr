from sqlalchemy import Column, VARCHAR, Integer

from db.models import BaseModel


class DBProductsCare(BaseModel):
    __tablename__ = 'Products_care'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(VARCHAR(), unique=True, nullable=False)
