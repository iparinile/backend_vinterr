from marshmallow import Schema, fields

from api.base import ResponseDto


class ResponseVariationInOrderDtoSchema(Schema):
    id = fields.Int(required=True)
    order_id = fields.Int(required=True)
    variation_id = fields.Int(required=True)
    amount = fields.Int(required=True)
    current_price = fields.Int(required=True)


class ResponseVariationInOrderDto(ResponseDto, ResponseVariationInOrderDtoSchema):
    __schema__ = ResponseVariationInOrderDtoSchema
