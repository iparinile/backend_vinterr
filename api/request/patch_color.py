from marshmallow import Schema, fields

from api.base import RequestDto


class RequestPatchColorDtoSchema(Schema):
    name = fields.Str()
    code = fields.Str()


class RequestPatchColorDto(RequestDto, RequestPatchColorDtoSchema):
    __schema__ = RequestPatchColorDtoSchema
    fields: list

    def __init__(self, *args, **kwargs):
        self.fields = []
        super(RequestPatchColorDto, self).__init__(*args, **kwargs)

    def set(self, key, value):
        self.fields.append(key)
        super(RequestPatchColorDto, self).set(key, value)
