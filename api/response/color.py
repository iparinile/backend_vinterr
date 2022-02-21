from marshmallow import Schema, fields

from api.base import ResponseDto


class ResponseColorDtoSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    code = fields.Str(required=True)


class ResponseColorDto(ResponseDto, ResponseColorDtoSchema):
    __schema__ = ResponseColorDtoSchema
