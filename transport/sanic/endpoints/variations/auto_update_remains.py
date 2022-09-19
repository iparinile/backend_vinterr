import os

from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.auto_update_remains import RequestAutoUpdateRemainsDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException
from db.queries import variations as variations_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException


class AutoUpdateRemainsEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestAutoUpdateRemainsDto(body)
        variations = {}
        for variation in request_model.variations_data:
            variations[variation['one_c_id']] = variation['amount']

        db_variations = variations_queries.get_all_variations(session)

        for db_variation in db_variations:
            if db_variation.variation_1c_id in variations.keys():
                db_variation.amount = variations[db_variation.variation_1c_id]
            else:
                db_variation.amount = 0

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        session.close_session()

        return await self.make_response_json(status=200)
