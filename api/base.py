from marshmallow import Schema, ValidationError, EXCLUDE
from sqlalchemy import MetaData

from api.exceptions import ApiValidationException, ApiResponseValidationException


class RequestDto:
    __schema__: Schema

    def __init__(self, data: dict):
        try:
            valid_data = self.__schema__(unknown=EXCLUDE).load(data)
        except ValidationError as error:
            raise ApiValidationException(error.messages)
        else:
            self._import(valid_data)

    def _import(self, data: dict):
        for name, field in data.items():
            self.set(name, field)

    def set(self, key, value):
        setattr(self, key, value)


class ResponseDto:
    __schema__: Schema

    def __init__(self, obj, many: bool = False, is_input_dict: bool = False):

        if many:
            properties = [self.parse_obj(o) for o in obj]
        elif is_input_dict:
            properties = obj
        else:
            properties = self.parse_obj(obj)

        try:
            self._data = self.__schema__(unknown=EXCLUDE, many=many).load(properties)
        except ValidationError as error:
            raise ApiResponseValidationException(error.messages)

    @staticmethod
    def parse_obj(obj: object) -> dict:
        result_dict = dict()
        for prop in dir(obj):
            if (not prop.startswith('_')) and (not prop.endswith('_')) and (not callable(getattr(obj, prop))) \
                    and (not isinstance(getattr(obj, prop), MetaData)):
                attr = getattr(obj, prop)
                if not isinstance(attr, (str, int, type(None))):
                    if isinstance(attr, list):
                        if len(attr) > 0:
                            if not type(attr[0]) is int:
                                result_dict[prop] = [ResponseDto.parse_obj(list_obj) for list_obj in attr]
                            else:
                                result_dict[prop] = attr
                        else:
                            result_dict[prop] = attr
                    else:
                        result_dict[prop] = ResponseDto.parse_obj(attr)
                else:
                    result_dict[prop] = attr
        return result_dict

    def dump(self) -> dict:
        return self._data
