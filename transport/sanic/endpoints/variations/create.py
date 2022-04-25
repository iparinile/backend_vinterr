from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.create_variation import RequestCreateVariationDto
from api.response.variation import ResponseVariationDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBGoodNotExistsException
from db.queries import goods as goods_queries
from db.queries import variations as variations_queries
from helpers.psycopg2_exceptions.get_details import get_details_psycopg2_exception
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicDBUniqueFieldException, SanicGoodNotFound


class CreateVariationEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateVariationDto(body)

        db_variation = variations_queries.create_variation(session, request_model)

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

        if request_model.is_default:
            try:
                goods_queries.set_default_variation(session, db_variation)
            except DBGoodNotExistsException:
                raise SanicGoodNotFound("Good not found")

            try:
                session.commit_session()
            except (DBDataException, DBIntegrityException) as e:
                raise SanicDBException(str(e))

        response_model = ResponseVariationDto(db_variation)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=201)
