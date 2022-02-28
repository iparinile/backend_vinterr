from typing import List

from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import sessionmaker, Session, Query

from db.exceptions import DBIntegrityException, DBDataException
from db.models import BaseModel, DBUsers, DBCustomers, DBMaterials, DBCategories, DBStructures, DBSizes, DBColors, \
    DBGoods, DBVariations


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

    '''
    requests to DBUsers
    '''

    def get_user_by_login(self, login: str) -> DBUsers:
        return self.query(DBUsers).filter(DBUsers.login == login).first()

    def get_user_by_id(self, user_id: int) -> DBUsers:
        return self.query(DBUsers).filter(DBUsers.id == user_id).first()

    '''
    requests to DBCustomers
    '''

    def get_customer_by_login(self, login: str) -> DBCustomers:
        return self.query(DBCustomers).filter(DBCustomers.login == login).first()

    def get_customer_by_email(self, email: str) -> DBCustomers:
        return self.query(DBCustomers).filter(DBCustomers.email == email).first()

    def get_customer_by_phone_number(self, phone_number: str) -> DBCustomers:
        return self.query(DBCustomers).filter(DBCustomers.phone_number == phone_number).first()

    '''
    requests to DBMaterials
    '''

    def get_material_by_name(self, material_name: str) -> DBMaterials:
        return self.query(DBMaterials).filter(DBMaterials.name == material_name).first()

    def get_material_by_id(self, material_id: int) -> DBMaterials:
        return self.query(DBMaterials).filter(DBMaterials.id == material_id).first()

    def get_all_materials(self) -> List['DBMaterials']:
        return self.query(DBMaterials).all()

    def delete_material(self, material_id: int):
        self.query(DBMaterials).filter(DBMaterials.id == material_id).delete()

    '''
    requests to DBCategories
    '''

    def get_category_by_name(self, category_name: str) -> DBCategories:
        return self.query(DBCategories).filter(DBCategories.name == category_name).first()

    def get_all_categories(self) -> List['DBCategories']:
        return self.query(DBCategories).all()

    def get_category_by_id(self, category_id: int) -> DBCategories:
        return self.query(DBCategories).filter(DBCategories.id == category_id).first()

    def delete_category(self, category_id: int):
        self.query(DBCategories).filter(DBCategories.id == category_id).delete()

    '''
    requests to DBStructures
    '''

    def get_structure_by_name(self, structure_name: str) -> DBStructures:
        return self.query(DBStructures).filter(DBStructures.name == structure_name).first()

    def get_all_structures(self) -> List['DBStructures']:
        return self.query(DBStructures).all()

    def get_structure_by_id(self, structure_id: int) -> DBStructures:
        return self.query(DBStructures).filter(DBStructures.id == structure_id).first()

    def delete_structure(self, structure_id: int):
        self.query(DBStructures).filter(DBStructures.id == structure_id).delete()

    '''
    requests to DBSizes
    '''

    def get_size_by_name(self, size_name: str) -> DBSizes:
        return self.query(DBSizes).filter(DBSizes.name == size_name).first()

    def get_all_sizes(self) -> List['DBSizes']:
        return self.query(DBSizes).all()

    def get_size_by_id(self, size_id: int) -> DBSizes:
        return self.query(DBSizes).filter(DBSizes.id == size_id).first()

    def delete_size(self, size_id: int):
        self.query(DBSizes).filter(DBSizes.id == size_id).delete()

    '''
    requests to DBColors
    '''

    def get_color_by_name(self, color_name: str) -> DBColors:
        return self.query(DBColors).filter(DBColors.name == color_name).first()

    def get_color_by_code(self, color_code: str) -> DBColors:
        return self.query(DBColors).filter(DBColors.code == color_code).first()

    def get_all_colors(self) -> List['DBColors']:
        return self.query(DBColors).all()

    def get_color_by_id(self, color_id: int) -> DBColors:
        return self.query(DBColors).filter(DBColors.id == color_id).first()

    def delete_color(self, color_id: int):
        self.query(DBColors).filter(DBColors.id == color_id).delete()

    '''
    requests to DBGoods
    '''

    def get_all_goods(self) -> List['DBGoods']:
        return self.query(DBGoods).all()

    def get_good_by_id(self, good_id: int) -> DBGoods:
        return self.query(DBGoods).filter(DBGoods.id == good_id).first()

    '''
    requests to DBVariations
    '''

    def get_all_variations(self) -> List['DBVariations']:
        return self.query(DBVariations).all()

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
