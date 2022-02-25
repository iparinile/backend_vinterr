from marshmallow import Schema, fields

from api.base import RequestDto


class RequestCreateGoodDtoSchema(Schema):
    name = fields.Str(required=True, allow_none=False)
    article = fields.Str(required=True, allow_none=False)
    good_1c_id = fields.Int(missing=None)
    category_id = fields.Int(required=True, allow_none=False)
    barcode = fields.Int(required=True, allow_none=False)
    structure_id = fields.Int(required=True, allow_none=False)
    # variations = fields.List(fields.Nested(VariationDtoSchema), required=True)


class RequestCreateGoodDto(RequestDto, RequestCreateGoodDtoSchema):
    __schema__ = RequestCreateGoodDtoSchema
