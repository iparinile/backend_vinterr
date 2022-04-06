from marshmallow import fields, Schema

from api.base import ResponseDto


class ResponseTelegramUserDtoSchema(Schema):
    chat_id = fields.Int(required=True, allow_none=False)
    status_id = fields.Int(required=True, allow_none=False)


class ResponseTelegramUserDto(ResponseDto, ResponseTelegramUserDtoSchema):
    __schema__ = ResponseTelegramUserDtoSchema
