import os

from dotenv import load_dotenv
from prettytable import PrettyTable
from sanic.request import Request
from sanic.response import BaseHTTPResponse
from telebot.apihelper import ApiTelegramException

from api.request.create_order import RequestCreateOrderDto
from api.response.order import ResponseOrderDto, VariationInOrderDto
from db.database import DBSession
from db.queries import cities as cities_queries
from db.queries import customers as customers_queries
from db.queries import customer_addresses as customer_addresses_queries
from db.queries import delivery_types as delivery_types_queries
from db.queries import orders as orders_queries
from db.queries import status_changes as status_changes_queries
from db.queries import streets as streets_queries
from db.queries import variations as variations_queries
from db.queries import variation_in_orders as variation_in_orders_queries
from db.exceptions import DBDataException, DBIntegrityException, DBCustomerNotExistsException, \
    DBVariationNotExistsException, DBVariationNegativeRest
from helpers.auth import read_token, ReadTokenException
from helpers.email.create_http_email_text import make_email_text
from helpers.email.sending_email import send_email
from helpers.psycopg2_exceptions.get_details import get_details_psycopg2_exception
from helpers.telegram_bot.send_message import send_message_to_chat
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicCustomerNotFound, SanicDBException, SanicDBUniqueFieldException, \
    SanicVariationNotFound, SanicInsufficientAmountVariation, SanicNoVariationsInOrder

load_dotenv()


class CreateOrderEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        request_model = RequestCreateOrderDto(body)

        if len(request_model.variations) == 0:
            raise SanicNoVariationsInOrder(message="There are no variations in the order")
        customer_is_registered = True
        token = ''

        try:
            token = read_token(request.token, '')
        except ReadTokenException:
            customer_is_registered = False

        if customer_is_registered:
            customer_id = token.get("customer_id")
            try:
                db_customer = customers_queries.get_customer(session, customer_id=customer_id)
            except DBCustomerNotExistsException:
                raise SanicCustomerNotFound('Customer not found')
        else:
            db_customer = customers_queries.create_unregistered_customer(session, request_model)

        session.add(db_customer)

        db_city = cities_queries.create_city(session, request_model.city)
        db_street = streets_queries.create_street(session, request_model.street)

        session.add(db_city)
        session.add(db_street)
        session.flush()

        db_customer_address = customer_addresses_queries.create_customer_addresses(
            session,
            body_request=request_model,
            customer=db_customer,
            city=db_city,
            street=db_street
        )

        session.add(db_customer_address)

        db_order = orders_queries.create_order(session, body_request=request_model, customer=db_customer)

        session.add(db_order)
        session.flush()

        variations_list = []
        for variation in request_model.variations:
            db_variation_in_order = variation_in_orders_queries.create_variation_in_order(
                session,
                variation_in_order=variation,
                order=db_order
            )
            variations_list.append(db_variation_in_order)

            db_variation = variations_queries.get_variations_by_id(session, db_variation_in_order.variation_id)
            try:
                variations_queries.buying_variations(db_variation, db_variation_in_order.amount)
            except DBVariationNegativeRest:
                raise SanicInsufficientAmountVariation(message="Insufficient number of variations in stock to order")

            session.add(db_variation_in_order)

        session.flush()
        variations_list = VariationInOrderDto(variations_list, many=True).dump()

        response_body = {
            "id": db_order.id,
            "customer_id": db_customer.id,
            "is_payed": db_order.is_payed,
            "status_id": db_order.status_id,
            "delivery_type_id": db_order.delivery_type_id,
            "city": db_city.name,
            "street": db_street.name,
            "house_number": db_customer_address.house_number,
            "apartment": db_customer_address.apartment,
            "other_info": db_customer_address.other_info,
            "is_cash_payment": db_order.is_cash_payment,
            "delivery_address": db_order.delivery_address,
            "delivery_cost": db_order.delivery_cost
        }

        response_model = ResponseOrderDto(response_body, is_input_dict=True)
        response_model = response_model.dump()
        response_model['variations'] = variations_list

        order_date = db_order.created_at.date()
        order_date = order_date.strftime("%d.%m.%Y")
        table_variations_in_order = PrettyTable()
        table_variations_in_order.field_names = ['Наименование', 'Количество', 'Цена']

        variations_in_order_list_to_email = []

        order_sum = 0
        for variation in variations_list:
            try:
                db_variation_in_order = variations_queries.get_variations_by_id(session, variation['variation_id'])
                table_variations_in_order.add_row(
                    [db_variation_in_order.name, variation['amount'], variation['current_price']])
                order_sum += variation['current_price'] * variation['amount']

                variations_in_order_list_to_email.append(
                    {
                        "name": db_variation_in_order.name,
                        "amount": variation['amount'],
                        "price": variation['current_price']
                    }
                )
            except DBVariationNotExistsException:
                raise SanicVariationNotFound(message=f"Variation id {variation['variation_id']} not found")

        db_delivery_type = delivery_types_queries.get_delivery_type_by_id(session, db_order.delivery_type_id)

        message = f"""
Оформлен заказ №{response_model['id']} от {order_date}

Клиент:
ФИО: {db_customer.second_name} {db_customer.first_name} {db_customer.last_name}
Телефон: {db_customer.phone_number}
Email: {db_customer.email}

Товары:
```{table_variations_in_order}```
Подытог: {order_sum} руб.

Тип доставки: {db_delivery_type.name}
Данные по доставке:
{db_order.delivery_address}
Стоимость: {db_order.delivery_cost} руб.

Итого: {db_order.delivery_cost + order_sum} руб.
Тип оплаты: {"наличными при получении" if db_order.is_cash_payment else "онлайн на сайте"}
"""
        message_to_customer = make_email_text(db_order, variations_in_order_list_to_email, order_sum, db_delivery_type)
        try:
            send_message_to_chat(chat_id=os.getenv("telegram_chat_id"), message=message)
        except ApiTelegramException as e:
            errors_chat_id = os.getenv('telegram_errors_chat_id')
            error_info = e.description
            error_info = error_info.replace("[", "\\[").replace("_", "\\_")
            send_message_to_chat(errors_chat_id, error_info)
        # await send_email(to_address=[os.getenv("email_to")], subject="Новый заказ на сайте", text=message_to_customer)
        send_email(to_address=[db_customer.email], subject="Данные по заказу Vinterr", text=message_to_customer)

        try:
            session.commit_session()
        except DBDataException as e:
            session.rollback()
            raise SanicDBException(str(e))
        except DBIntegrityException as e:
            session.rollback()
            exception_code, exception_info = get_details_psycopg2_exception(e)
            if exception_code == '23505':
                raise SanicDBUniqueFieldException(exception_info)
            else:
                raise SanicDBException(str(e))

        db_status_changes = status_changes_queries.create_status_changes(session, db_order.id, db_order.status_id)
        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        session.close_session()

        return await self.make_response_json(body=response_model, status=201)
