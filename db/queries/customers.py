from api.request.create_customer import RequestCreateCustomerDtoSchema
from api.request.create_order import RequestCreateOrderDto
from db.database import DBSession
from db.exceptions import DBCustomerLoginExistsException, DBCustomerEmailExistsException, \
    DBCustomerPhoneNumberExistsException, DBCustomerNotExistsException
from db.models import DBCustomers


def create_customer(
        session: DBSession,
        customer: RequestCreateCustomerDtoSchema,
        hashed_password: bytes
) -> DBCustomers:
    new_customer = DBCustomers(
        login=customer.login,
        password=hashed_password,
        first_name=customer.first_name,
        second_name=customer.second_name,
        last_name=customer.last_name,
        email=customer.email,
        birthday=customer.birthday,
        phone_number=customer.phone_number,
        is_registered=True
    )

    if session.get_customer_by_login(new_customer.login) is not None:
        raise DBCustomerLoginExistsException
    elif session.get_customer_by_email(new_customer.email) is not None:
        raise DBCustomerEmailExistsException
    elif session.get_customer_by_phone_number(new_customer.phone_number) is not None:
        raise DBCustomerPhoneNumberExistsException

    session.add_model(new_customer)

    return new_customer


def get_customer(session: DBSession, login: str = None, customer_id: int = None) -> DBCustomers:
    db_customer = None

    if login is not None:
        db_customer = session.get_customer_by_login(login)
    elif customer_id is not None:
        db_customer = session.get_customer_by_id(customer_id)

    if db_customer is None:
        raise DBCustomerNotExistsException
    return db_customer


def create_unregistered_customer(session: DBSession, body_request: RequestCreateOrderDto) -> DBCustomers:
    new_customer = DBCustomers(
        first_name=body_request.first_name,
        second_name=body_request.second_name,
        last_name=body_request.last_name,
        phone_number=body_request.phone_number,
        email=body_request.email
    )
    # db_customer = session.get_customer_by_phone_number(new_customer.phone_number)
    # if db_customer is not None:
    #     return db_customer
    # db_customer = session.get_customer_by_email(new_customer.email)
    # if db_customer is not None:
    #     return db_customer

    session.add_model(new_customer)

    return new_customer

# def patch_customer(customer: DBCustomers, patch_fields_customer: RequestPatchUserDto) -> DBCustomers:
#     for attr in patch_fields_user.fields:
#         if hasattr(patch_fields_user, attr):
#             value = getattr(patch_fields_user, attr)
#             setattr(customer, attr, value)
#     return customer
