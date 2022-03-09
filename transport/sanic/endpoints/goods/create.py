from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.create_good import RequestCreateGoodDto
from api.response.good import ResponseGoodDto
from db.exceptions import DBDataException, DBIntegrityException
from db.queries import goods as goods_queries
from helpers.psycopg2_exceptions.get_details import get_details_psycopg2_exception
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicDBUniqueFieldException


class CreateGoodEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateGoodDto(body)

        db_good = goods_queries.create_good(session, request_model)

        try:
            session.commit_session()
        except DBDataException as e:
            raise SanicDBException(str(e))
        except DBIntegrityException as e:
            exception_code, exception_info = get_details_psycopg2_exception(e)
            if exception_code == '23505':
                raise SanicDBUniqueFieldException(exception_info)
            else:
                raise SanicDBException(str(e))

        response_model = ResponseGoodDto(db_good)

        return await self.make_response_json(body=response_model.dump(), status=201)
