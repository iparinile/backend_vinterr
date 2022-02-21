from marshmallow import fields, Schema

from api.base import RequestDto


class RequestCreateDirectoryItemDtoSchema(Schema):
    name = fields.Str(required=True, allow_none=False)


class RequestCreateMaterialDto(RequestDto, RequestCreateDirectoryItemDtoSchema):
    __schema__ = RequestCreateDirectoryItemDtoSchema


class RequestCreateCategoryDto(RequestDto, RequestCreateDirectoryItemDtoSchema):
    __schema__ = RequestCreateDirectoryItemDtoSchema


class RequestCreateStructureDto(RequestDto, RequestCreateDirectoryItemDtoSchema):
    __schema__ = RequestCreateDirectoryItemDtoSchema


class RequestCreateSizeDto(RequestDto, RequestCreateDirectoryItemDtoSchema):
    __schema__ = RequestCreateDirectoryItemDtoSchema
