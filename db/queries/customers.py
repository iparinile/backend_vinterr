from api.request.create_customer import RequestCreateCustomerDtoSchema
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


def get_customer(session: DBSession, login: str = None) -> DBCustomers:
    db_customer = None

    if login is not None:
        db_customer = session.get_customer_by_login(login)

    if db_customer is None:
        raise DBCustomerNotExistsException
    return db_customer
