from marshmallow import fields, Schema

from api.base import RequestDto


class RequestCreateColorDtoSchema(Schema):
    name = fields.Str(required=True, allow_none=False)
    code = fields.Str(required=True, allow_none=False)


class RequestCreateColorDto(RequestDto, RequestCreateColorDtoSchema):
    __schema__ = RequestCreateColorDtoSchema
