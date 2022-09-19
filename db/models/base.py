import datetime

from sqlalchemy import Column, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(
        TIMESTAMP,
        nullable=False,
        default=datetime.datetime.utcnow
    )

    update_at = Column(
        TIMESTAMP,
        nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )

    def __repr__(self):
        return f'{self.__class__.__name__}'
