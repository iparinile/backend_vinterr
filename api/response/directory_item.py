from marshmallow import fields, Schema

from api.base import ResponseDto


class ResponseCreateDirectoryItemDtoSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)


class ResponseCreateMaterialDto(ResponseDto, ResponseCreateDirectoryItemDtoSchema):
    __schema__ = ResponseCreateDirectoryItemDtoSchema
