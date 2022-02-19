from typing import List

from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import sessionmaker, Session, Query

from db.exceptions import DBIntegrityException, DBDataException
from db.models import BaseModel, DBUsers, DBCustomers, DBMaterials


class DBSession:
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    def query(self, *args, **kwargs) -> Query:
        return self._session.query(*args, **kwargs)

    def delete_rows(self, model) -> Query:
        return self.query(model).delete()

    def close_session(self):
        self._session.close()

    def get_user_by_login(self, login: str) -> DBUsers:
        return self.query(DBUsers).filter(DBUsers.login == login).first()

    def get_user_by_id(self, user_id: int) -> DBUsers:
        return self.query(DBUsers).filter(DBUsers.id == user_id).first()

    def get_customer_by_login(self, login: str) -> DBCustomers:
        return self.query(DBCustomers).filter(DBCustomers.login == login).first()

    def get_customer_by_email(self, email: str) -> DBCustomers:
        return self.query(DBCustomers).filter(DBCustomers.email == email).first()

    def get_customer_by_phone_number(self, phone_number: str) -> DBCustomers:
        return self.query(DBCustomers).filter(DBCustomers.phone_number == phone_number).first()

    def get_material_by_name(self, material_name: str) -> DBMaterials:
        return self.query(DBMaterials).filter(DBMaterials.name == material_name).first()

    def get_material_by_id(self, material_id: int) -> DBMaterials:
        return self.query(DBMaterials).filter(DBMaterials.id == material_id).first()

    def get_all_materials(self) -> List['DBMaterials']:
        return self.query(DBMaterials).all()

    def delete_material(self, material_id: int):
        self.query(DBMaterials).filter(DBMaterials.id == material_id).delete()

    def add_model(self, model: BaseModel):
        try:
            self._session.add(model)
        except IntegrityError as e:
            raise DBIntegrityException(e)
        except DataError as e:
            raise DBDataException(e)

    def commit_session(self, need_close: bool = False):
        try:
            self._session.commit()
        except IntegrityError as e:
            raise DBIntegrityException(e)
        except DataError as e:
            raise DBDataException(e)

        if need_close:
            self.close_session()


class DataBase:
    connexion: Engine
    session_factory: sessionmaker
    _test_query = 'SELECT 1'

    def __init__(self, connection: Engine):
        self.connexion = connection
        self.session_factory = sessionmaker(bind=self.connexion)

    def check_connection(self):
        self.connexion.execute(self._test_query).fetchone()

    def make_session(self) -> DBSession:
        session = self.session_factory()
        return DBSession(session)
