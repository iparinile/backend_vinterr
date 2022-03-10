from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.create_order import RequestCreateOrderDto
from db.queries import cities as cities_queries
from db.queries import customers as customers_queries
from db.queries import customer_addresses as customer_addresses_queries
from db.queries import orders as orders_queries
from db.queries import regions as regions_queries
from db.queries import streets as streets_queries
from db.queries import variation_in_orders as variation_in_orders_queries
from db.exceptions import DBDataException, DBIntegrityException, DBCustomerNotExistsException
from helpers.auth import read_token, ReadTokenException
from helpers.psycopg2_exceptions.get_details import get_details_psycopg2_exception
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicCustomerNotFound, SanicDBException, SanicDBUniqueFieldException


class CreateOrderEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:
        request_model = RequestCreateOrderDto(body)

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

        try:
            session.commit_session()
        except DBDataException as e:
            raise SanicDBException(str(e))
        except DBIntegrityException as e:
            exception_code, exception_info = get_details_psycopg2_exception(e)
            if exception_code == '23505':
                raise SanicDBUniqueFieldException(exception_info)
            else:
                raise SanicDBException(str(e))

        db_region = regions_queries.create_region(session, request_model.region)
        db_city = cities_queries.create_city(session, request_model.city)
        db_street = streets_queries.create_city(session, request_model.street)

        try:
            session.commit_session()
        except DBDataException as e:
            raise SanicDBException(str(e))
        except DBIntegrityException as e:
            exception_code, exception_info = get_details_psycopg2_exception(e)
            if exception_code == '23505':
                raise SanicDBUniqueFieldException(exception_info)
            else:
                raise SanicDBException(str(e))

        db_customer_address = customer_addresses_queries.create_customer_addresses(
            session,
            body_request=request_model,
            customer=db_customer,
            region=db_region,
            city=db_city,
            street=db_street
        )

        try:
            session.commit_session()
        except DBDataException as e:
            raise SanicDBException(str(e))
        except DBIntegrityException as e:
            exception_code, exception_info = get_details_psycopg2_exception(e)
            if exception_code == '23505':
                raise SanicDBUniqueFieldException(exception_info)
            else:
                raise SanicDBException(str(e))

        db_order = orders_queries.create_order(session, body_request=request_model, customer=db_customer)
        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        variations_list = []
        for variation in request_model.variations:
            db_variation = variation_in_orders_queries.create_variation_in_order(
                session,
                variation_in_order=variation,
                order=db_order
            )
            variations_list.append(db_variation)
        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(body=request_model.dump(), status=201)
