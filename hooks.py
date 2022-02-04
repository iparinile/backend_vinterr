from sqlalchemy import create_engine

from configs.config import ApplicationConfig
from context import Context
from db.database import DataBase


def init_db_postgres(config: ApplicationConfig, context: Context):
    engine = create_engine(
        config.database.url,
        pool_pre_ping=True,
    )
    database = DataBase(connection=engine)
    database.check_connection()

    context.set('database', database)
