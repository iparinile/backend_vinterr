from marshmallow import Schema, fields

from api.base import RequestDto


class RequestPatchGoodDtoSchema(Schema):
    name = fields.Str()
    article = fields.Str()
    good_1c_id = fields.Str()
    category_id = fields.Int()
    barcode = fields.Str()
    structure_id = fields.Int()
    description = fields.Str()
    is_visible = fields.Bool()


class RequestPatchGoodDto(RequestDto, RequestPatchGoodDtoSchema):
    __schema__ = RequestPatchGoodDtoSchema
    fields: list

    def __init__(self, *args, **kwargs):
        self.fields = []
        super(RequestPatchGoodDto, self).__init__(*args, **kwargs)

    def set(self, key, value):
        self.fields.append(key)
        super(RequestPatchGoodDto, self).set(key, value)
