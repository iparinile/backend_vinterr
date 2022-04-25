from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.create_directory_item import RequestCreateDeliveryTypeDto
from api.response.directory_item import ResponseDeliveryTypeDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBDeliveryTypeExistsException
from db.queries import delivery_types as delivery_types_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicDeliveryTypeConflictException


class CreateDeliveryTypeEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateDeliveryTypeDto(body)

        try:
            db_delivery_type = delivery_types_queries.create_delivery_type(session, request_model)
        except DBDeliveryTypeExistsException:
            raise SanicDeliveryTypeConflictException('Delivery type with this name exists')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseDeliveryTypeDto(db_delivery_type)

        session.close_session()

        return await self.make_response_json(body=response_model.dump(), status=201)
