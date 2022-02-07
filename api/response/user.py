from marshmallow import Schema, fields

from api.base import ResponseDto


class ResponseUserDtoSchema(Schema):
    id = fields.Int(required=True)
    login = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    group_id = fields.Int()


class ResponseUserDto(ResponseDto, ResponseUserDtoSchema):
    __schema__ = ResponseUserDtoSchema
