from marshmallow import Schema, fields

from api.base import ResponseDto


class ResponseCreateVariationDtoSchema(Schema):
    good_id = fields.Int(required=True)
    name = fields.Str(required=True)
    color_id = fields.Int(required=True)
    size_id = fields.Int(required=True)
    price = fields.Int(required=True)
    variation_1c_id = fields.Str(required=True, allow_none=True)
    amount = fields.Int(required=True)
    barcode = fields.Str(required=True)
    is_sale = fields.Bool(required=True)
    is_new = fields.Bool(required=True)


class ResponseCreateVariationDto(ResponseDto, ResponseCreateVariationDtoSchema):
    __schema__ = ResponseCreateVariationDtoSchema
