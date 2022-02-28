from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response.good import ResponseCreateGoodDto
from db.database import DBSession
from db.queries import goods as goods_queries
from transport.sanic.endpoints import BaseEndpoint


class GetAllGoodsEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        goods = goods_queries.get_all_goods(session)

        response_model = ResponseCreateGoodDto(goods, many=True)

        return await self.make_response_json(status=200, body=response_model.dump())
