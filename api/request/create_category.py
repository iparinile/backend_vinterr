from marshmallow import fields, Schema

from api.base import RequestDto


class RequestCreateCategoryDtoSchema(Schema):
    name = fields.Str(required=True, allow_none=False)
    parent_id = fields.Str(missing=None)


class RequestCreateCategoryDto(RequestDto, RequestCreateCategoryDtoSchema):
    __schema__ = RequestCreateCategoryDtoSchema
