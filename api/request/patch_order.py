from marshmallow import Schema, fields

from api.base import RequestDto


class RequestPatchOrderDtoSchema(Schema):
    id = fields.Int()
    is_payed = fields.Bool()
    customer_id = fields.Int()
    status_id = fields.Int()
    delivery_type_id = fields.Int()
    sberbank_id = fields.Str()
    delivery_address = fields.Str()
    delivery_cost = fields.Float()


class RequestPatchOrderDto(RequestDto, RequestPatchOrderDtoSchema):
    __schema__ = RequestPatchOrderDtoSchema
    fields: list

    def __init__(self, *args, **kwargs):
        self.fields = []
        super(RequestPatchOrderDto, self).__init__(*args, **kwargs)

    def set(self, key, value):
        self.fields.append(key)
        super(RequestPatchOrderDto, self).set(key, value)
