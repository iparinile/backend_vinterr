import os

from sanic.request import Request
from sanic.response import BaseHTTPResponse

from db.database import DBSession
from transport.sanic.endpoints import BaseEndpoint


class ImageEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, img_path: str,
                         *args, **kwargs) -> BaseHTTPResponse:
        image_url = f"{os.getcwd()}/src/img/{img_path}"
        return await self.make_response_file(file_url=image_url)
