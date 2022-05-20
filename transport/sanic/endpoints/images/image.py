import os
from pathlib import Path

from sanic.request import Request
from sanic.response import BaseHTTPResponse

from db.database import DBSession
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicWrongImagePath


class ImageEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, img_path: str,
                         *args, **kwargs) -> BaseHTTPResponse:
        image_url = f"{os.getcwd()}/src/img/{img_path}"

        if not Path(image_url).is_file():
            raise SanicWrongImagePath(message="Wrong image path")
        return await self.make_response_file(file_url=image_url)
