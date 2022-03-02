from marshmallow import fields, Schema

from api.base import ResponseDto


class ResponseCategoryDtoSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)


class ResponseCategoryDto(ResponseDto, ResponseCategoryDtoSchema):
    __schema__ = ResponseCategoryDtoSchema
