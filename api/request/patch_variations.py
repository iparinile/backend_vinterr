from marshmallow import Schema, fields

from api.base import RequestDto


class RequestPatchVariationDtoSchema(Schema):
    good_id = fields.Int()
    name = fields.Str()
    color_id = fields.Int()
    size_id = fields.Int()
    price = fields.Int()
    discounted_price = fields.Int()
    variation_1c_id = fields.Str()
    amount = fields.Int()
    barcode = fields.Str()
    is_sale = fields.Bool()
    is_new = fields.Bool()


class RequestPatchVariationDto(RequestDto, RequestPatchVariationDtoSchema):
    __schema__ = RequestPatchVariationDtoSchema
    fields: list

    def __init__(self, *args, **kwargs):
        self.fields = []
        super(RequestPatchVariationDto, self).__init__(*args, **kwargs)

    def set(self, key, value):
        self.fields.append(key)
        super(RequestPatchVariationDto, self).set(key, value)
