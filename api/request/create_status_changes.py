from marshmallow import fields, Schema

from api.base import RequestDto


class RequestCreateStatusChangesDtoSchema(Schema):
    order_id = fields.Int(required=True, allow_none=False)
    status_id = fields.Int(required=True, allow_none=False)


class RequestCreateStatusChangesDto(RequestDto, RequestCreateStatusChangesDtoSchema):
    __schema__ = RequestCreateStatusChangesDtoSchema
