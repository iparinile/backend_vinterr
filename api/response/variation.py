from marshmallow import Schema, fields

from api.base import ResponseDto


class ResponseVariationDtoSchema(Schema):
    id = fields.Int(required=True)
    good_id = fields.Int(required=True)
    name = fields.Str(required=True)
    color_id = fields.Int(required=True)
    size_id = fields.Int(required=True)
    price = fields.Int(required=True)
    discounted_price = fields.Int(missing=None)
    variation_1c_id = fields.Str(required=True, allow_none=True)
    amount = fields.Int(required=True)
    barcode = fields.Str(required=True, allow_none=True)
    is_sale = fields.Bool(required=True)
    is_new = fields.Bool(required=True)
    # images = fields.List(fields.Nested(ResponseImageDtoSchema), missing=None)


class ResponseVariationDto(ResponseDto, ResponseVariationDtoSchema):
    __schema__ = ResponseVariationDtoSchema
