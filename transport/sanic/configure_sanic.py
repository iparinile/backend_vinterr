from sanic import Sanic
from sanic_openapi import openapi3_blueprint

from configs.config import ApplicationConfig
from context import Context
from hooks import init_db_postgres
from transport.sanic.routes import get_routes


def configure_app(config: ApplicationConfig, context: Context):

    init_db_postgres(config, context)

    app = Sanic(__name__)
    app.blueprint(openapi3_blueprint)
    app.config.API_VERSION = "0.1.0"
    app.config.API_TITLE = "Backend_vinterr_API"

    for handler in get_routes(config, context):
        app.add_route(
            handler=handler,
            uri=handler.uri,
            methods=handler.methods,
            strict_slashes=True,
        )

    return app
