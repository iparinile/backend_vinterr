from os import path, mkdir

from sanic.request import Request, File
from sanic.response import BaseHTTPResponse

from api.request.update_remains import RequestUploadFileDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException
from db.queries import goods as goods_queries
from helpers.excel.parse_weights import parse_weights
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException


class UpdateWeightsEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestUploadFileDto(request.files)

        excel_file: File = request_model.file
        excel_body: bytes = excel_file.body

        excel_path = "src/excel"
        exel_name = excel_file.name
        if not path.isdir(excel_path):
            mkdir(excel_path)
        excel_path += "/" + exel_name

        new_excel_file = open(excel_path, mode="wb")
        new_excel_file.write(excel_body)
        new_excel_file.close()

        weights_data = parse_weights(excel_path)

        db_goods = goods_queries.get_all_goods_only(session)

        for db_good in db_goods:
            if db_good.article in weights_data.keys():
                db_good.weight = weights_data[db_good.article]
            else:
                db_good.weight = None

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        session.close_session()

        return await self.make_response_json(status=200)
