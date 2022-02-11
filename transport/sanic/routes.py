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
        endpoints.CreateCustomerEndpoint(config=config, context=context, uri='/customer', methods=['POST']),
        endpoints.AuthCustomerEndpoint(config=config, context=context, uri='/customer/auth', methods=['POST'])
    )
