import datetime

from marshmallow import Schema, fields, pre_load, post_load

from api.base import ResponseDto


class ResponseCustomerDtoSchema(Schema):
    id = fields.Int(required=True)
    login = fields.Str(required=True)
    first_name = fields.Str(required=True)
    second_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(missing=None)
    birthday = fields.Date(missing=None)
    phone_number = fields.Str(required=True)

    @pre_load
    @post_load
    def deserialize_date(self, data: dict, **kwargs) -> dict:
        if 'birthday' in data:
            data['birthday'] = self.date_to_iso(data['birthday'])

        return data

    @staticmethod
    def date_to_iso(dt):
        if isinstance(dt, datetime.date):
            return dt.isoformat()
        return dt


class ResponseCustomerDto(ResponseDto, ResponseCustomerDtoSchema):
    __schema__ = ResponseCustomerDtoSchema
