from marshmallow import Schema, fields

from api.base import ResponseDto


class VariationDtoSchema(Schema):
    name = fields.Str(required=True)
    color_id = fields.Int(required=True)
    size_id = fields.Int(required=True)
    price = fields.Int(required=True)
    variation_1c_id = fields.Int(missing=None)
    amount = fields.Int(required=True)
    barcode = fields.Int(required=True)
    is_sale = fields.Bool(missing=None)
    is_new = fields.Bool(missing=None)
    is_default = fields.Bool(missing=None)


class ResponseGoodDtoSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    article = fields.Str(required=True)
    good_1c_id = fields.Str(missing=None)
    category_id = fields.Int(required=True)
    barcode = fields.Str(missing=None)
    structure_id = fields.Int(required=True)
    products_care_id = fields.Int(missing=None)
    description = fields.Str(missing=None)
    is_visible = fields.Bool(required=True)
    default_variation = fields.Int(missing=None)
    # variations = fields.List(fields.Nested(VariationDtoSchema), required=True)


class ResponseGoodDto(ResponseDto, ResponseGoodDtoSchema):
    __schema__ = ResponseGoodDtoSchema
