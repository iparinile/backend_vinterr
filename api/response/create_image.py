from marshmallow import fields, Schema

from api.base import ResponseDto


class ResponseCreateImageDtoSchema(Schema):
    image_url = fields.Str(required=True)
    variation_id = fields.Int(required=True)


class ResponseCreateImageDto(ResponseDto, ResponseCreateImageDtoSchema):
    __schema__ = ResponseCreateImageDtoSchema
