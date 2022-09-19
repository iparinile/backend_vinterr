from marshmallow import fields, Schema, EXCLUDE

from api.base import RequestDto


class VariationAmountDtoSchema(Schema):
    one_c_id = fields.Str(required=True, allow_none=False)
    amount = fields.Int(required=True, allow_none=False)


class RequestAutoUpdateRemainsDtoSchema(Schema):
    variations_data = fields.List(fields.Nested(VariationAmountDtoSchema, unknown=EXCLUDE), required=True)


class RequestAutoUpdateRemainsDto(RequestDto, RequestAutoUpdateRemainsDtoSchema):
    __schema__ = RequestAutoUpdateRemainsDtoSchema
