import datetime

from marshmallow import fields, Schema, pre_load, post_load

from api.base import ResponseDto


class ResponseStatusChangesDtoSchema(Schema):
    id = fields.Int(required=True)
    order_id = fields.Int(required=True)
    status_id = fields.Int(required=True)
    created_at = fields.DateTime(required=True)

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


class ResponseStatusChangesDto(ResponseDto, ResponseStatusChangesDtoSchema):
    __schema__ = ResponseStatusChangesDtoSchema
