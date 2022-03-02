from marshmallow import Schema, fields

from api.base import RequestDto


class RequestCreateCustomerDtoSchema(Schema):
    first_name = fields.Str(required=True, allow_none=False)
    second_name = fields.Str(required=True, allow_none=False)
    last_name = fields.Str(required=True, allow_none=False)
    login = fields.Str(missing=None)
    password = fields.Str(missing=None)
    email = fields.Str(missing=None)
    birthday = fields.Date(missing=None)
    phone_number = fields.Str(required=True, allow_none=False)


class RequestCreateCustomerDto(RequestDto, RequestCreateCustomerDtoSchema):
    __schema__ = RequestCreateCustomerDtoSchema
