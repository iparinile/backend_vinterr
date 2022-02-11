from marshmallow import Schema, fields

from api.base import RequestDto


class RequestAuthCustomerDtoSchema(Schema):
    login = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)


class RequestAuthCustomerDto(RequestDto, RequestAuthCustomerDtoSchema):
    __schema__ = RequestAuthCustomerDtoSchema
