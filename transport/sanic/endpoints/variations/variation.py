from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.patch_variations import RequestPatchVariationDto
from api.response.variation import ResponseVariationDto
from db.database import DBSession
from db.exceptions import DBVariationNotExistsException, DBDataException, DBIntegrityException
from db.queries import variations as variations_queries
from helpers.psycopg2_exceptions.get_details import get_details_psycopg2_exception
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicVariationNotFound, SanicDBException, SanicDBUniqueFieldException


class VariationEndpoint(BaseEndpoint):
    async def method_delete(self, request: Request, body: dict, session: DBSession, variation_id: int,
                            *args, **kwargs) -> BaseHTTPResponse:

        try:
            variation = variations_queries.get_variations_by_id(session, variation_id)
        except DBVariationNotExistsException:
            raise SanicVariationNotFound('Variation not found')

        variations_queries.delete_variation(variation)

        try:
            session.commit_session(need_close=True)
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)
    async def method_patch(self, request: Request, body: dict, session: DBSession, variation_id: int,
                           *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestPatchVariationDto(body)

        try:
            variation = variations_queries.get_variations_by_id(session, variation_id)
        except DBVariationNotExistsException:
            raise SanicVariationNotFound('Variation not found')

        variation = variations_queries.patch_variation(variation, request_model)

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

        response_model = ResponseVariationDto(variation)

        session.close_session()
        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_options(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:

        headers_response = {"Allow": "PATCH,OPTIONS"}
        return await self.make_response_json(headers=headers_response, status=200)
