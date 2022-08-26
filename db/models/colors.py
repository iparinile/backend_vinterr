from sqlalchemy import Column, Integer, VARCHAR

from db.models import BaseModel


class DBColors(BaseModel):
    __tablename__ = 'Colors'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(VARCHAR(255), unique=True, nullable=False)
    code = Column(VARCHAR(50), nullable=False)
