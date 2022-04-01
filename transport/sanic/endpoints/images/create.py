from sanic.request import Request
from sanic.response import BaseHTTPResponse

from db.database import DBSession
from transport.sanic.endpoints import BaseEndpoint


class CreateImageEndpoint(BaseEndpoint):
    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        # for file in request.files:
        pass
