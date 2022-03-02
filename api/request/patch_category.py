from marshmallow import Schema, fields

from api.base import RequestDto


class RequestPatchCategoryDtoSchema(Schema):
    name = fields.Str()
    code = fields.Str()


class RequestPatchCategoryDto(RequestDto, RequestPatchCategoryDtoSchema):
    __schema__ = RequestPatchCategoryDtoSchema
    fields: list

    def __init__(self, *args, **kwargs):
        self.fields = []
        super(RequestPatchCategoryDto, self).__init__(*args, **kwargs)

    def set(self, key, value):
        self.fields.append(key)
        super(RequestPatchCategoryDto, self).set(key, value)
