from typing import Tuple

from configs.config import ApplicationConfig
from context import Context
from transport.sanic import endpoints


def get_routes(config: ApplicationConfig, context: Context) -> Tuple:
    return (
        endpoints.HealthEndpoint(config=config, context=context, uri='/', methods=['GET', 'POST']),
        endpoints.CreateUserEndpoint(config=config, context=context, uri='/users', methods=['POST'],
                                     auth_required=True, is_administrator_access=True),
        endpoints.AuthUserEndpoint(config=config, context=context, uri='/users/auth', methods=['POST']),
        endpoints.UserEndpoint(config=config, context=context, uri='/users/<user_id:int>', methods=['GET'],
                               auth_required=True, is_administrator_access=True),
        endpoints.CreateCustomerEndpoint(config=config, context=context, uri='/customers', methods=['POST']),
        endpoints.AuthCustomerEndpoint(config=config, context=context, uri='/customers/auth', methods=['POST']),
        endpoints.GetAllMaterialsEndpoint(config=config, context=context, uri='/materials/all', methods=['GET']),
        endpoints.CreateMaterialEndpoint(config=config, context=context, uri='/materials', methods=['POST'],
                                         auth_required=True, is_administrator_access=True),
        endpoints.MaterialEndpoint(config=config, context=context, uri='/materials/<material_id:int>',
                                   methods=['GET', 'PATCH', 'DELETE'],
                                   auth_required=True, is_administrator_access=True),
    )
