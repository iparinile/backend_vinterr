from marshmallow import fields, Schema

from api.base import ResponseDto


class ResponseRegisterPaymentDtoSchema(Schema):
    order_id = fields.Int(required=True)
    amount = fields.Float(required=True)
    sberbank_order_id = fields.Str(required=True)
    payment_form_url = fields.Str(required=True)


class ResponseRegisterPaymentDto(ResponseDto, ResponseRegisterPaymentDtoSchema):
    __schema__ = ResponseRegisterPaymentDtoSchema
