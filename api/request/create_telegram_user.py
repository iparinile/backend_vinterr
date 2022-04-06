from marshmallow import fields, Schema

from api.base import RequestDto


class RequestCreateTelegramUserDtoSchema(Schema):
    chat_id = fields.Int(required=True, allow_none=False)


class RequestCreateTelegramUserDto(RequestDto, RequestCreateTelegramUserDtoSchema):
    __schema__ = RequestCreateTelegramUserDtoSchema
