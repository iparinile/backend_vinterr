from marshmallow import Schema, fields

from api.base import ResponseDto


class ResponseAuthDtoSchema(Schema):
    user_id = fields.Int(required=True)
    Authorization = fields.Str(required=True)


class ResponseAuthDto(ResponseDto, ResponseAuthDtoSchema):
    __schema__ = ResponseAuthDtoSchema
