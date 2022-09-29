from marshmallow import fields, Schema

from api.base import RequestDto


class RequestRegisterPaymentDtoSchema(Schema):
    order_id = fields.Int(required=True)
    amount = fields.Float(required=True)
    return_url = fields.Str(required=True)
    fail_url = fields.Str(required=True)
    shipping_cost = fields.Float(required=True)


class RequestRegisterPaymentDto(RequestDto, RequestRegisterPaymentDtoSchema):
    __schema__ = RequestRegisterPaymentDtoSchema
