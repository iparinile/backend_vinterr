from marshmallow import Schema, fields

from api.base import RequestDto


class VariationsInOrderDtoSchema(Schema):
    variation_id = fields.Int(required=True)
    amount = fields.Int(required=True)
    current_price = fields.Int(required=True)


class RequestCreateOrderDtoSchema(Schema):
    # Customer info
    first_name = fields.Str(required=True)
    second_name = fields.Str(required=True)
    last_name = fields.Str(missing=None)
    phone_number = fields.Str(required=True)
    email = fields.Str(required=True)
    # Order info
    status_id = fields.Int(required=True)
    delivery_type_id = fields.Int(required=True)
    # Address info
    city = fields.Str(required=True)
    street = fields.Str(required=True)
    house_number = fields.Str(missing=None)
    apartment = fields.Str(missing=None)
    other_info = fields.Str(missing=None)
    delivery_address = fields.Str(missing=None)
    delivery_cost = fields.Float(missing=0)
    is_cash_payment = fields.Bool(missing=False)

    variations = fields.List(fields.Nested(VariationsInOrderDtoSchema), required=True)


class RequestCreateOrderDto(RequestDto, RequestCreateOrderDtoSchema):
    __schema__ = RequestCreateOrderDtoSchema


class VariationsInOrderDto(RequestDto, VariationsInOrderDtoSchema):
    __schema__ = VariationsInOrderDtoSchema
