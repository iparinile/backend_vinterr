from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from db.models import BaseModel


class DBImages(BaseModel):
    __tablename__ = 'Images'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    url = Column(VARCHAR(255), nullable=False)
    variation_id = Column(Integer, ForeignKey('Variations.id', ondelete='CASCADE'), nullable=False)
    model_info = Column(VARCHAR(255), default=None)
