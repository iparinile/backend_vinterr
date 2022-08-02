import os
from pathlib import Path

from sanic.request import Request
from sanic.response import BaseHTTPResponse

from db.database import DBSession
from db.exceptions import DBImageNotExistsException, DBDataException, DBIntegrityException
from db.queries.images import get_image_by_url
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicWrongImagePath, SanicDBException


class ImageEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, img_path: str,
                         *args, **kwargs) -> BaseHTTPResponse:
        image_url = f"{os.getcwd()}/src/img/{img_path}"

        if not Path(image_url).is_file():
            raise SanicWrongImagePath(message="Wrong image path")
        return await self.make_response_file(file_url=image_url)

    async def method_delete(self, request: Request, body: dict, session: DBSession, img_path: str,
                            *args, **kwargs) -> BaseHTTPResponse:

        try:
            db_image = get_image_by_url(session, img_path)
        except DBImageNotExistsException:
            raise SanicWrongImagePath(message="Wrong image path")

        session.delete_image(db_image.id)
        try:
            session.commit_session(need_close=True)
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)
