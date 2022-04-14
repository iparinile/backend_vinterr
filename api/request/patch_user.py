from marshmallow import Schema, fields

from api.base import RequestDto


class RequestPatchUserDtoSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    login = fields.Str()
    password = fields.Str()


class RequestPatchUserDto(RequestDto, RequestPatchUserDtoSchema):
    __schema__ = RequestPatchUserDtoSchema
    fields: list

    def __init__(self, *args, **kwargs):
        self.fields = []
        super(RequestPatchUserDto, self).__init__(*args, **kwargs)

    def set(self, key, value):
        self.fields.append(key)
        super(RequestPatchUserDto, self).set(key, value)
