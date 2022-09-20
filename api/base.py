import json
import os

from marshmallow import Schema, ValidationError, EXCLUDE
from sqlalchemy import MetaData

from api.exceptions import ApiValidationException, ApiResponseValidationException
from helpers.telegram_bot.send_message import send_message_to_chat


class RequestDto:
    __schema__: Schema

    def __init__(self, data: dict):
        try:
            valid_data = self.__schema__(unknown=EXCLUDE).load(data)
        except ValidationError as error:
            errors_chat_id = os.getenv('telegram_errors_chat_id')
            try:
                error_info = json.dumps(data)
                send_message_to_chat(errors_chat_id, error_info)
            except Exception:
                pass
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
        return {
            prop: value
            for prop in dir(obj)
            if not prop.startswith('_')
               and not prop.endswith('_')
               and not callable(value := getattr(obj, prop))
        }

    def dump(self) -> dict:
        return self._data
