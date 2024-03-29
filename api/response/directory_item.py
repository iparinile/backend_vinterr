from marshmallow import fields, Schema

from api.base import ResponseDto


class ResponseDirectoryItemDtoSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)


class ResponseMaterialDto(ResponseDto, ResponseDirectoryItemDtoSchema):
    __schema__ = ResponseDirectoryItemDtoSchema


class ResponseStructureDto(ResponseDto, ResponseDirectoryItemDtoSchema):
    __schema__ = ResponseDirectoryItemDtoSchema


class ResponseSizeDto(ResponseDto, ResponseDirectoryItemDtoSchema):
    __schema__ = ResponseDirectoryItemDtoSchema


class ResponseStatusDto(ResponseDto, ResponseDirectoryItemDtoSchema):
    __schema__ = ResponseDirectoryItemDtoSchema


class ResponseDeliveryTypeDto(ResponseDto, ResponseDirectoryItemDtoSchema):
    __schema__ = ResponseDirectoryItemDtoSchema


class ResponseProductsCareDto(ResponseDto, ResponseDirectoryItemDtoSchema):
    __schema__ = ResponseDirectoryItemDtoSchema
