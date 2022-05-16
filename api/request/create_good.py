from marshmallow import Schema, fields

from api.base import RequestDto


class RequestCreateGoodDtoSchema(Schema):
    name = fields.Str(required=True, allow_none=False)
    article = fields.Str(required=True, allow_none=False)
    good_1c_id = fields.Str(missing=None)
    category_id = fields.Int(required=True, allow_none=False)
    barcode = fields.Str(missing=None)
    structure_id = fields.Int(required=True, allow_none=False)
    description = fields.Str(required=True, allow_none=False)
    is_visible = fields.Bool(missing=True)
    # variations = fields.List(fields.Nested(VariationDtoSchema), required=True)


class RequestCreateGoodDto(RequestDto, RequestCreateGoodDtoSchema):
    __schema__ = RequestCreateGoodDtoSchema
