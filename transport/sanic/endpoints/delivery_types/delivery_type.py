from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.patch_directory_item import RequestPatchDeliveryTypeDto
from api.response.directory_item import ResponseDeliveryTypeDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBDeliveryTypeNotExistsException
from db.queries import delivery_types as delivery_types_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicDeliveryTypeNotFound


class DeliveryTypeEndpoint(BaseEndpoint):

    async def method_patch(self, request: Request, body: dict, session: DBSession, delivery_type_id: int,
                           *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestPatchDeliveryTypeDto(body)

        try:
            delivery_type = delivery_types_queries.get_delivery_type_by_id(session, delivery_type_id)
        except DBDeliveryTypeNotExistsException:
            raise SanicDeliveryTypeNotFound('Delivery type not found')

        delivery_type = delivery_types_queries.patch_delivery_type(delivery_type, request_model.name)

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseDeliveryTypeDto(delivery_type)

        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_delete(self, request: Request, body: dict, session: DBSession, delivery_type_id: int,
                            *args, **kwargs) -> BaseHTTPResponse:

        try:
            delivery_type = delivery_types_queries.get_delivery_type_by_id(session, delivery_type_id)
        except DBDeliveryTypeNotExistsException:
            raise SanicDeliveryTypeNotFound('Delivery type not found')

        delivery_types_queries.delete_delivery_type(session, delivery_type.id)

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)

    async def method_get(self, request: Request, body: dict, session: DBSession, delivery_type_id: int,
                         *args, **kwargs) -> BaseHTTPResponse:

        try:
            delivery_type = delivery_types_queries.get_delivery_type_by_id(session, delivery_type_id)
        except DBDeliveryTypeNotExistsException:
            raise SanicDeliveryTypeNotFound('Delivery type not found')

        response_model = ResponseDeliveryTypeDto(delivery_type)

        return await self.make_response_json(body=response_model.dump(), status=200)
