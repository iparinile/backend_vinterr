from marshmallow import fields, Schema

from api.base import RequestDto


class RequestUploadFileDtoSchema(Schema):
    file = fields.Raw(type='file', required=True, allow_none=False)


class RequestUploadFileDto(RequestDto, RequestUploadFileDtoSchema):
    __schema__ = RequestUploadFileDtoSchema
