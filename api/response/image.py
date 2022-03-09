from marshmallow import Schema, fields

from api.base import ResponseDto


class ResponseImageDtoSchema(Schema):
    id = fields.Int(required=True)
    url = fields.Str(required=True)
    model_info = fields.Str(missing=None)


class ResponseImageDto(ResponseDto, ResponseImageDtoSchema):
    __schema__ = ResponseImageDtoSchema
