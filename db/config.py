import os
from dotenv import load_dotenv

load_dotenv()


class PostgresConfig:
    name = os.getenv('dbname', 'test')
    host = os.getenv("db_host", "localhost")
    user = os.getenv("db_user", "postgres")
    password = os.getenv("db_password", "1")
    url = f'postgresql+psycopg2://{user}:{password}@{host}/{name}'
