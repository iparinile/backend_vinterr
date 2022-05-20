from marshmallow import Schema, fields

from api.base import RequestDto


class RequestCreateImageDtoSchema(Schema):
    image = fields.Raw(type='file', required=True, allow_none=False)


class RequestCreateImageDto(RequestDto, RequestCreateImageDtoSchema):
    __schema__ = RequestCreateImageDtoSchema
