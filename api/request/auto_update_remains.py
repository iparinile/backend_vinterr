from marshmallow import fields, Schema

from api.base import RequestDto


class RequestAutoUpdateRemainsDtoSchema(Schema):
    amount = fields.Str(required=True, allow_none=False)
    one_c_id = fields.Str(required=True, allow_none=False)


class RequestAutoUpdateRemainsDto(RequestDto, RequestAutoUpdateRemainsDtoSchema):
    __schema__ = RequestAutoUpdateRemainsDtoSchema
