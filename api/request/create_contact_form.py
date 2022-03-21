from marshmallow import Schema, fields

from api.base import RequestDto


class RequestCreateContactFormDtoSchema(Schema):
    customer_name = fields.Str(required=True, allow_none=False)
    phone_number = fields.Str(required=True, allow_none=False)
    text = fields.Str(missing=None)
    email = fields.Str(missing=None)


class RequestCreateContactFormDto(RequestDto, RequestCreateContactFormDtoSchema):
    __schema__ = RequestCreateContactFormDtoSchema
