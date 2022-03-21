from marshmallow import Schema, fields

from api.base import ResponseDto


class ResponseCreateContactFormDtoSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    customer_name = fields.Str(required=True, allow_none=False)
    phone_number = fields.Str(required=True, allow_none=False)
    text = fields.Str(missing=None)
    email = fields.Str(missing=None)


class ResponseCreateContactFormDto(ResponseDto, ResponseCreateContactFormDtoSchema):
    __schema__ = ResponseCreateContactFormDtoSchema
