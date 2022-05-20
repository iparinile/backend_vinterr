import os

from sanic.request import Request, File
from sanic.response import BaseHTTPResponse

from api.request.create_image import RequestCreateImageDto
from db.database import DBSession
from db.exceptions import DBVariationNotExistsException, DBDataException, DBIntegrityException
from db.queries.images import create_image
from db.queries.variations import get_variations_by_id
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicIncorrectRequest, SanicVariationNotFound, SanicDBException


class CreateImageEndpoint(BaseEndpoint):
    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        request_model = RequestCreateImageDto(request.files)

        if (len(request.args) != 1) or ("variation_id" not in request.args.keys()):
            raise SanicIncorrectRequest(message="Incorrect request")

        variation_id = request.args["variation_id"][0]
        try:
            db_variation = get_variations_by_id(session, variation_id)
        except DBVariationNotExistsException:
            raise SanicVariationNotFound('Variation not found')
        image: File = request_model.image
        image_body: bytes = image.body

        images_path = "src/img"
        images_folders = os.scandir(images_path)
        folders_counter = 0
        for _ in images_folders:
            folders_counter += 1
        latest_images_path = f"{images_path}/{folders_counter}"

        files = os.listdir(path=latest_images_path)
        files_amount = len(files)

        if files_amount >= 100:
            latest_images_path = f"{images_path}/{folders_counter + 1}"
            os.mkdir(latest_images_path)

        image_path = f"{latest_images_path}/{image.name}"
        image_path_in_db = f"{folders_counter}/{image.name}"
        new_image = open(image_path, mode="wb")
        new_image.write(image_body)
        new_image.close()

        db_images = create_image(session, variation_id, image_path_in_db)

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        image_url = f"https://backend.vinterr-plus.ru/images/{db_images.url}"
        response_body = {
            "image_url": image_url,
            "variation_id": variation_id
        }

        return await self.make_response_json(body=response_body, status=201)
