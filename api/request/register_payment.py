from marshmallow import fields, Schema

from api.base import RequestDto


class RequestRegisterPaymentDtoSchema(Schema):
    order_id = fields.Int(required=True)
    return_url = fields.Str(required=True)
    fail_url = fields.Str(required=True)


class RequestRegisterPaymentDto(RequestDto, RequestRegisterPaymentDtoSchema):
    __schema__ = RequestRegisterPaymentDtoSchema
