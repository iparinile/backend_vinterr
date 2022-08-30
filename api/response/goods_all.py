from marshmallow import Schema, fields

from api.base import ResponseDto
from api.response.image import ResponseImageDtoSchema


class VariationDtoSchema(Schema):
    id = fields.Int(required=True)
    good_id = fields.Int(required=True)
    name = fields.Str(required=True)
    color_id = fields.Int(required=True)
    size_id = fields.Int(required=True)
    price = fields.Int(required=True)
    discounted_price = fields.Int(missing=None)
    variation_1c_id = fields.Str(required=True, allow_none=True)
    amount = fields.Int(required=True)
    is_sale = fields.Bool(required=True)
    is_new = fields.Bool(required=True)
    images = fields.List(fields.Nested(ResponseImageDtoSchema), required=True)


class SizeDtoSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)


class ColorDtoSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    code = fields.Str(required=True)
    # sizes = fields.List(fields.Nested(SizeDtoSchema), required=True)


class ResponseGoodsAllDtoSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    article = fields.Str(required=True)
    category_id = fields.Int(required=True)
    structure_id = fields.Int(required=True)
    description = fields.Str(missing=None)
    is_visible = fields.Bool(required=True)
    default_variation = fields.Int(missing=None)

    # variations = fields.List(fields.Nested(VariationDtoSchema), required=True)
    colors = fields.List(fields.Nested(ColorDtoSchema), many=True, required=True)
    variations_to_show = fields.List(fields.Int(), required=True)


class ResponseGoodsAllDto(ResponseDto, ResponseGoodsAllDtoSchema):
    __schema__ = ResponseGoodsAllDtoSchema
