from marshmallow import Schema, fields

from api.base import RequestDto


class RequestCreateCustomerDtoSchema(Schema):
    first_name = fields.Str(required=True, allow_none=False)
    last_name = fields.Str(required=True, allow_none=False)
    login = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)
    email = fields.Str(required=True, allow_none=False)
    birthday = fields.Date(required=True, allow_none=False)
    phone_number = fields.Str(required=True, allow_none=False)


class RequestCreateCustomerDto(RequestDto, RequestCreateCustomerDtoSchema):
    __schema__ = RequestCreateCustomerDtoSchema
