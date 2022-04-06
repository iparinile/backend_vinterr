from sqlalchemy import Column, Integer

from db.models import BaseModel


class DBTelegramUsers(BaseModel):
    __tablename__ = 'Telegram_users'

    chat_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    status_id = Column(Integer, nullable=False)
