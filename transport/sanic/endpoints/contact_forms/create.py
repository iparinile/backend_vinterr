import os

from dotenv import load_dotenv
from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.create_contact_form import RequestCreateContactFormDto
from api.response.contact_form import ResponseCreateContactFormDto
from db.exceptions import DBDataException, DBIntegrityException
from db.queries.contact_forms import create_contact_forms
from helpers.psycopg2_exceptions.get_details import get_details_psycopg2_exception
from helpers.telegram_bot.send_message import send_message_to_chat
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicDBUniqueFieldException

load_dotenv()


class CreateContactFormEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:
        request_model = RequestCreateContactFormDto(body)

        db_contact_forms = create_contact_forms(session, request_model)

        try:
            session.commit_session()
        except DBDataException as e:
            raise SanicDBException(str(e))
        except DBIntegrityException as e:
            exception_code, exception_info = get_details_psycopg2_exception(e)
            if exception_code in ['23503', '23505']:
                raise SanicDBUniqueFieldException(exception_info)
            else:
                raise SanicDBException(str(e))

        message = f"""
Новое сообщение №{db_contact_forms.id}\n
Имя клиента: {db_contact_forms.customer_name}
Телефон: {db_contact_forms.phone_number}
"""
        if db_contact_forms.email is not None:
            message += f"Email: {db_contact_forms.email}"
        if db_contact_forms.text is not None:
            message += f"Текст обращения: {db_contact_forms.text}"

        send_message_to_chat(chat_id=os.getenv("telegram_chat_id"), message=message)

        response_model = ResponseCreateContactFormDto(db_contact_forms).dump()

        return await self.make_response_json(body=response_model, status=201)
