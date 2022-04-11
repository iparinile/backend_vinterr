from api.request.create_order import RequestCreateOrderDto
from db.database import DBSession
from db.models import DBCustomerAddresses, DBCustomers, DBCities, DBStreets


def create_customer_addresses(
        session: DBSession,
        body_request: RequestCreateOrderDto,
        customer: DBCustomers,
        city: DBCities,
        street: DBStreets
) -> DBCustomerAddresses:
    new_customer_addresses = DBCustomerAddresses(
        customer_id=customer.id,
        city_id=city.id,
        streets_id=street.id,
        house_number=body_request.house_number,
        apartment=body_request.apartment,
        other_info=body_request.other_info
    )

    session.add_model(new_customer_addresses)

    return new_customer_addresses
