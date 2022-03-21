from api.request.create_contact_form import RequestCreateContactFormDto
from db.database import DBSession
from db.models.contact_forms import DBContactForms


def create_contact_forms(session: DBSession, contact_form: RequestCreateContactFormDto) -> DBContactForms:
    new_contact_form = DBContactForms(
        customer_name=contact_form.customer_name,
        phone_number=contact_form.phone_number,
        text=contact_form.text,
        email=contact_form.email
    )

    session.add_model(new_contact_form)

    return new_contact_form
