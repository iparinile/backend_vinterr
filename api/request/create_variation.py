from marshmallow import Schema, fields

from api.base import RequestDto


class RequestCreateVariationDtoSchema(Schema):
    good_id = fields.Int(required=True, allow_none=False)
    name = fields.Str(required=True, allow_none=False)
    color_id = fields.Int(required=True, allow_none=False)
    size_id = fields.Int(required=True, allow_none=False)
    price = fields.Int(required=True, allow_none=False)
    discounted_price = fields.Int(missing=None)
    variation_1c_id = fields.Str(missing=None)
    amount = fields.Int(required=True, allow_none=False)
    barcode = fields.Str(missing=None)
    is_sale = fields.Bool(missing=False)
    is_new = fields.Bool(missing=False)
    is_default = fields.Bool(missing=None)


class RequestCreateVariationDto(RequestDto, RequestCreateVariationDtoSchema):
    __schema__ = RequestCreateVariationDtoSchema
