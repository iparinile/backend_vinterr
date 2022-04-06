from marshmallow import Schema, fields

from api.base import RequestDto


class RequestPatchTelegramUserDtoSchema(Schema):
    chat_id = fields.Int()
    status_id = fields.Int()


class RequestPatchTelegramUserDto(RequestDto, RequestPatchTelegramUserDtoSchema):
    __schema__ = RequestPatchTelegramUserDtoSchema
    fields: list

    def __init__(self, *args, **kwargs):
        self.fields = []
        super(RequestPatchTelegramUserDto, self).__init__(*args, **kwargs)

    def set(self, key, value):
        self.fields.append(key)
        super(RequestPatchTelegramUserDto, self).set(key, value)
