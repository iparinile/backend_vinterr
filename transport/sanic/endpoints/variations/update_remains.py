from os import path, mkdir

from sanic.request import Request, File
from sanic.response import BaseHTTPResponse

from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBVariationNotExistsException
from db.queries import variations as variations_queries
from helpers.excel.parse_remains import parse_remains
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException


class UpdateRemainsEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        files = request.files

        excel_file: File = files.get('file')
        excel_body: bytes = excel_file.body

        excel_path = "src/excel"
        exel_name = excel_file.name
        if not path.isdir(excel_path):
            mkdir(excel_path)
        excel_path += "/" + exel_name

        new_excel_file = open(excel_path, mode="wb")
        new_excel_file.write(excel_body)
        new_excel_file.close()

        remains_data = parse_remains(excel_path)

        db_variations = variations_queries.get_all_variations(session)

        for db_variation in db_variations:
            if db_variation.variation_1c_id in remains_data.keys():
                db_variation.amount = remains_data[db_variation.variation_1c_id]
            else:
                db_variation.amount = 0

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        session.close_session()

        return await self.make_response_json(status=200)
