from typing import List

from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import sessionmaker, Session, Query

from db.exceptions import DBIntegrityException, DBDataException
from db.models import BaseModel, DBUsers, DBCustomers, DBMaterials, DBCategories, DBStructures, DBSizes, DBColors, \
    DBGoods, DBVariations, DBImages, DBCities, DBStreets, DBOrders, DBStatuses, DBDeliveryTypes, \
    DBVariationInOrders, DBTelegramUsers


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

    def get_customer_by_id(self, customer_id: int) -> DBCustomers:
        return self.query(DBCustomers).filter(DBCustomers.id == customer_id).first()

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

    def get_all_categories(self, params: dict) -> List['DBCategories']:
        query = self.query(DBCategories)
        for param_name in params.keys():
            query = query.filter(getattr(DBCategories, param_name) == params[param_name][0])
        return query.all()

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

    def get_all_goods(self, request_params: dict) -> List['DBGoods']:
        query = self.query(DBGoods, DBVariations, DBColors, DBSizes, DBImages)
        query = query.filter(DBGoods.is_delete == False)
        query = query.filter(DBVariations.is_delete == False)
        query = query.outerjoin(DBVariations, DBVariations.good_id == DBGoods.id)
        if "category_id" in request_params.keys():
            query = query.filter(DBGoods.category_id == request_params["category_id"][0])
        if "color_id" in request_params.keys():
            query = query.filter(DBVariations.color_id == request_params["color_id"][0])
        if "size_id" in request_params.keys():
            query = query.filter(DBVariations.size_id == request_params["size_id"][0])
        query = query.outerjoin(DBColors, DBColors.id == DBVariations.color_id)
        query = query.outerjoin(DBSizes, DBSizes.id == DBVariations.size_id)
        query = query.outerjoin(DBImages, DBImages.variation_id == DBVariations.id)

        return query.all()

    def get_good_by_id(self, good_id: int) -> DBGoods:
        query = self.query(DBGoods, DBCategories, DBStructures)
        query = query.filter(DBGoods.is_delete == False)
        query = query.filter(DBGoods.id == good_id)
        return query.first()

    '''
    requests to DBVariations
    '''

    def get_all_variations(self) -> List['DBVariations']:
        return self.query(DBVariations).filter(DBVariations.is_delete == False).all()

    def get_variations_by_good_id(self, good_id: int) -> List['DBVariations']:
        query = self.query(DBVariations, DBColors, DBSizes)
        query = query.filter(DBVariations.is_delete == False)
        query = query.outerjoin(DBColors, DBColors.id == DBVariations.color_id)
        query = query.outerjoin(DBSizes, DBSizes.id == DBVariations.size_id)
        query = query.filter(DBVariations.good_id == good_id)
        return query.all()

    def get_variation_by_id(self, variation_id: int) -> DBVariations:
        return self.query(DBVariations).filter(DBVariations.id == variation_id).first()

    def get_variation_by_id_with_full_info(self, variation_id: int) -> DBVariations:
        query = self.query(DBVariations, DBColors, DBSizes)
        query = query.filter(DBVariations.is_delete == False)
        query = query.outerjoin(DBColors, DBColors.id == DBVariations.color_id)
        query = query.outerjoin(DBSizes, DBSizes.id == DBVariations.size_id)
        query = query.filter(DBVariations.id == variation_id)
        return query.first()

    def get_variation_by_1c_id(self, one_c_id: str) -> DBVariations:
        return self.query(DBVariations).filter(DBVariations.variation_1c_id == one_c_id)

    '''
    requests to DBImages
    '''

    def get_images_by_variation_id(self, variation_id: int) -> List['DBImages']:
        return self.query(DBImages).filter(DBImages.variation_id == variation_id).all()

    '''
    requests to DBCities
    '''

    def get_city_by_name(self, city_name: str) -> DBCities:
        return self.query(DBCities).filter(DBCities.name == city_name).first()

    '''
    requests to DBStreets
    '''

    def get_street_by_name(self, street_name: str) -> DBStreets:
        return self.query(DBStreets).filter(DBStreets.name == street_name).first()

    def add_model(self, model: BaseModel):
        try:
            self._session.add(model)
        except IntegrityError as e:
            raise DBIntegrityException(e)
        except DataError as e:
            raise DBDataException(e)

    '''
    requests to DBOrders
    '''

    def order_query(self) -> Query:
        query = self.query(DBOrders, DBCustomers, DBStatuses, DBDeliveryTypes, DBVariationInOrders, DBVariations,
                           DBColors, DBSizes, DBGoods, DBCategories)
        query = query.outerjoin(DBCustomers, DBCustomers.id == DBOrders.customer_id)
        query = query.outerjoin(DBStatuses, DBStatuses.id == DBOrders.status_id)
        query = query.outerjoin(DBDeliveryTypes, DBDeliveryTypes.id == DBOrders.delivery_type_id)
        query = query.outerjoin(DBVariationInOrders, DBVariationInOrders.order_id == DBOrders.id)
        query = query.outerjoin(DBVariations, DBVariations.id == DBVariationInOrders.variation_id)
        query = query.outerjoin(DBColors, DBColors.id == DBVariations.color_id)
        query = query.outerjoin(DBSizes, DBSizes.id == DBVariations.size_id)
        query = query.outerjoin(DBGoods, DBGoods.id == DBVariations.good_id)
        query = query.outerjoin(DBCategories, DBCategories.id == DBGoods.category_id)
        return query

    def get_all_orders(self) -> List['DBOrders']:
        query = self.order_query()
        return query.all()

    def get_order(self, order_id) -> DBOrders:
        query = self.order_query()
        query = query.filter(DBOrders.id == order_id)
        return query.first()

    def get_order_by_id(self, order_id: int) -> DBOrders:
        return self.query(DBOrders).filter(DBOrders.id == order_id).all()

    def get_order_by_sberbank_id(self, sberbank_id: str) -> DBOrders:
        query = self.query(DBOrders).filter(DBOrders.sberbank_id == sberbank_id)
        return query.first()

    '''
    requests to DBDeliveryTypes
    '''

    def get_delivery_type_by_id(self, delivery_type_id: int) -> DBDeliveryTypes:
        return self.query(DBDeliveryTypes).filter(DBDeliveryTypes.id == delivery_type_id).first()

    def get_delivery_type_by_name(self, delivery_type_name: str) -> DBDeliveryTypes:
        return self.query(DBDeliveryTypes).filter(DBDeliveryTypes.name == delivery_type_name).first()

    def get_all_delivery_types(self) -> List['DBDeliveryTypes']:
        return self.query(DBDeliveryTypes).all()

    def delete_delivery_type(self, delivery_type_id: int) -> DBDeliveryTypes:
        return self.query(DBDeliveryTypes).filter(DBDeliveryTypes.id == delivery_type_id).delete()

    '''
    requests to DBStatuses
    '''

    def get_status_by_name(self, status_name: str) -> DBStatuses:
        return self.query(DBStatuses).filter(DBStatuses.name == status_name).first()

    def get_all_statuses(self) -> List['DBStatuses']:
        return self.query(DBStatuses).all()

    def get_status_by_id(self, status_id: int) -> DBStatuses:
        return self.query(DBStatuses).filter(DBStatuses.id == status_id).first()

    def delete_status(self, status_id: int):
        self.query(DBStatuses).filter(DBStatuses.id == status_id).delete()

    '''
    requests to DBTelegramUsers
    '''

    def get_telegram_user_by_id(self, user_id: int) -> DBTelegramUsers:
        return self.query(DBTelegramUsers).filter(DBTelegramUsers.chat_id == user_id).first()

    '''
----------------------------------------------------------------------------------
    '''

    def commit_session(self, need_close: bool = False):
        try:
            self._session.commit()
        except IntegrityError as e:
            raise DBIntegrityException(e)
        except DataError as e:
            raise DBDataException(e)

        if need_close:
            self.close_session()

    def rollback(self):
        self._session.rollback()

    def flush(self):
        self._session.flush()

    def add(self, model):
        self._session.add(model)


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
