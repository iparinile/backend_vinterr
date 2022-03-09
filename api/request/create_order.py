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
    last_name = fields.Str(required=True)
    phone_number = fields.Str(required=True)
    # Order info
    status_id = fields.Int(required=True)
    delivery_type_id = fields.Int(required=True)
    # Address info
    region = fields.Str(required=True)
    city = fields.Str(required=True)
    street = fields.Str(required=True)
    house_number = fields.Int(required=True)
    apartment = fields.Int(required=True)
    other_info = fields.Str(missing=None)

    variations = fields.List(fields.Nested(VariationsInOrderDtoSchema), required=True)


class RequestCreateOrderDto(RequestDto, RequestCreateOrderDtoSchema):
    __schema__ = RequestCreateOrderDtoSchema


class VariationsInOrderDto(RequestDto, VariationsInOrderDtoSchema):
    __schema__ = VariationsInOrderDtoSchema
