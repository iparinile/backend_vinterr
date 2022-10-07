import os
from http import HTTPStatus
from typing import Iterable, Union

from sanic.request import Request
from sanic.response import BaseHTTPResponse, json, file

from configs.config import ApplicationConfig
from context import Context
from helpers.auth import ReadTokenException, read_token
from helpers.telegram_bot.send_message import send_message_to_chat
from transport.sanic.exceptions import SanicAuthException


class SanicEndpoint:

    async def __call__(self, request: Request, *args, **kwargs):
        if self.auth_required:
            if self.is_administrator_access:
                role = 'admin'
            else:
                role = ''
            try:
                token = {
                    'token': self.import_body_auth(request, role)
                }
            except SanicAuthException as e:
                return await self.make_response_json(status=e.status_code)
            else:
                kwargs.update(token)
        elif self.telegram_password_required:
            if not self.is_telegram_password_correct(request):
                return await self.make_response_json(status=401)
        return await self.handler(request, *args, **kwargs)

    def __init__(
            self,
            config: ApplicationConfig,
            context: Context,
            uri: str,
            methods: Iterable,
            auth_required: bool = False,
            telegram_password_required: bool = False,
            is_administrator_access: bool = False,
            *args, **kwargs
    ):
        self.config = config
        self.uri = uri
        self.methods = methods
        self.context = context
        self.auth_required = auth_required
        self.telegram_password_required = telegram_password_required
        self.is_administrator_access = is_administrator_access
        self.__name__ = self.__class__.__name__

    @staticmethod
    async def make_response_json(
            headers: dict = None, body: Union[dict, list] = None, status: int = 200, message: str = None,
            error_code: int = None
    ) -> BaseHTTPResponse:

        if body is None:
            body = {
                'message': message or HTTPStatus(status).phrase,
                'error_code': error_code or status
            }

        if (str(status).startswith("5")) or (str(error_code).startswith("5"))\
                or (str(status).startswith("4")) or (str(error_code).startswith("4")):
            errors_chat_id = os.getenv('telegram_errors_chat_id')
            error_info = ''.join('{}{}'.format(key, val) for key, val in body.items())
            error_info = error_info.replace("[", "\\[").replace("_", "\\_")
            send_message_to_chat(errors_chat_id, error_info)
        return json(headers=headers, body=body, status=status)

    @staticmethod
    async def make_response_file(file_url: str) -> BaseHTTPResponse:
        return await file(location=file_url)

    @staticmethod
    def import_body_json(request: Request) -> dict:
        if 'application/json' in request.content_type and request.json is not None:
            return dict(request.json)
        return {}

    @staticmethod
    def import_body_headers(request: Request) -> dict:
        return {
            header: value
            for header, value in request.headers.items()
            if header.lower().startswith('x-')
        }

    @staticmethod
    def import_body_auth(request: Request, role: str) -> dict:
        token = request.headers.get('Authorization')
        try:
            return read_token(token, role)
        except ReadTokenException as e:
            raise SanicAuthException(str(e))

    @staticmethod
    def is_telegram_password_correct(request: Request) -> bool:
        password = request.headers.get('Authorization')
        if password == os.getenv("telegram_secret_password"):
            return True
        else:
            return False

    async def handler(self, request: Request, *args, **kwargs) -> BaseHTTPResponse:
        body = {}

        # if self.auth_required:
        #     try:
        #         body.update(self.import_body_auth(request))
        #     except SanicAuthException as e:
        #         return await self.make_response_json(status=e.status_code)

        body.update(self.import_body_json(request))
        body.update(self.import_body_headers(request))

        return await self._method(request, body, *args, **kwargs)

    async def _method(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        method = request.method.lower()
        func_name = f'method_{method}'

        if hasattr(self, func_name):
            func = getattr(self, func_name)
            return await func(request, body, *args, **kwargs)
        return await self.method_not_impl(method=method)

    async def method_not_impl(self, method: str) -> BaseHTTPResponse:
        return await self.make_response_json(status=200, message=f'Method {method.upper()} not implemented')

    async def method_get(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.method_not_impl(method='GET')

    async def method_post(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.method_not_impl(method='POST')

    async def method_patch(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.method_not_impl(method='PATCH')

    async def method_delete(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.method_not_impl(method='DELETE')

    async def method_options(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.method_not_impl(method='OPTIONS')
