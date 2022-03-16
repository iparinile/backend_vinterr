from marshmallow import fields, Schema

from api.base import ResponseDto


class VariationsInOrderDtoSchema(Schema):
    id = fields.Int(required=True)
    variation_id = fields.Int(required=True)
    amount = fields.Int(required=True)
    current_price = fields.Int(required=True)


class ResponseOrderDtoSchema(Schema):
    id = fields.Int(required=True)
    # Order info
    customer_id = fields.Int(required=True)
    is_payed = fields.Bool(required=True)
    status_id = fields.Int(required=True)
    delivery_type_id = fields.Int(required=True)
    # Address info
    region = fields.Str(required=True)
    city = fields.Str(required=True)
    street = fields.Str(required=True)
    house_number = fields.Int(required=True)
    apartment = fields.Int(required=True)
    other_info = fields.Str(missing=None)


class ResponseOrderDto(ResponseDto, ResponseOrderDtoSchema):
    __schema__ = ResponseOrderDtoSchema
