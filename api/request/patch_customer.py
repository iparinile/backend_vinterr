from marshmallow import Schema, fields

from api.base import RequestDto


class RequestPatchCustomerDtoSchema(Schema):
    first_name = fields.Str()
    second_name = fields.Str()
    last_name = fields.Str()
    login = fields.Str()
    password = fields.Str()
    email = fields.Str()
    birthday = fields.Date()
    phone_number = fields.Str()


class RequestPatchCustomerDto(RequestDto, RequestPatchCustomerDtoSchema):
    __schema__ = RequestPatchCustomerDtoSchema
    fields: list

    def __init__(self, *args, **kwargs):
        self.fields = []
        super(RequestPatchCustomerDto, self).__init__(*args, **kwargs)

    def set(self, key, value):
        self.fields.append(key)
        super(RequestPatchCustomerDto, self).set(key, value)
