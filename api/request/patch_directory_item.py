from marshmallow import Schema, fields

from api.base import RequestDto


class RequestPatchDirectoryItemDtoSchema(Schema):
    name = fields.Str(required=True)


class RequestPatchMaterialDto(RequestDto, RequestPatchDirectoryItemDtoSchema):
    __schema__ = RequestPatchDirectoryItemDtoSchema
