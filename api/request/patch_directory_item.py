from marshmallow import Schema, fields

from api.base import RequestDto


class RequestPatchDirectoryItemDtoSchema(Schema):
    name = fields.Str(required=True)


class RequestPatchMaterialDto(RequestDto, RequestPatchDirectoryItemDtoSchema):
    __schema__ = RequestPatchDirectoryItemDtoSchema


class RequestPatchStructureDto(RequestDto, RequestPatchDirectoryItemDtoSchema):
    __schema__ = RequestPatchDirectoryItemDtoSchema


class RequestPatchSizeDto(RequestDto, RequestPatchDirectoryItemDtoSchema):
    __schema__ = RequestPatchDirectoryItemDtoSchema


class RequestPatchStatusDto(RequestDto, RequestPatchDirectoryItemDtoSchema):
    __schema__ = RequestPatchDirectoryItemDtoSchema
