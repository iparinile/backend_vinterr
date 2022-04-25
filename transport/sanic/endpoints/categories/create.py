from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.create_category import RequestCreateCategoryDto
from api.response.category import ResponseCategoryDto
from db.database import DBSession
from db.exceptions import DBCategoryExistsException, DBDataException, DBIntegrityException
from db.queries import categories as categories_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicCategoryConflictException, SanicDBException


class CreateCategoryEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateCategoryDto(body)

        try:
            db_category = categories_queries.create_category(session, request_model)
        except DBCategoryExistsException:
            raise SanicCategoryConflictException('Category with this name exists')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseCategoryDto(db_category)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=201)
