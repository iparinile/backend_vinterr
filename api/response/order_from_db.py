import datetime

from marshmallow import fields, Schema, pre_load, post_load

from api.base import ResponseDto


class ResponseOrderDBDtoSchema(Schema):
    id = fields.Int(required=True)
    is_payed = fields.Bool(required=True)
    created_at = fields.DateTime(required=True)
    customer_id = fields.Int(required=True)
    status_id = fields.Int(required=True)
    delivery_type_id = fields.Int(required=True)
    sberbank_id = fields.Str(missing=None)
    delivery_address = fields.Str(missing=None)
    delivery_cost = fields.Float(missing=0)

    @pre_load
    @post_load
    def deserialize_datetime(self, data: dict, **kwargs) -> dict:
        if 'created_at' in data:
            data['created_at'] = self.datetime_to_iso(data['created_at'])

        return data

    @staticmethod
    def datetime_to_iso(dt):
        if isinstance(dt, datetime.datetime):
            return dt.isoformat()
        return dt


class ResponseOrderDBDto(ResponseDto, ResponseOrderDBDtoSchema):
    __schema__ = ResponseOrderDBDtoSchema
