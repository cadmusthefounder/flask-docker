import logging.config
import os

from flask import Flask, Response, request
from flask_cors import CORS
from flask_injector import FlaskInjector
from flask_log_request_id import RequestID, current_request_id

from flask_docker.common.configurations import LOGGING_CONFIG
from flask_docker.common.helper import is_development, is_testing
from flask_docker.server.error_handler import ErrorHandler
from flask_docker.server.module import RelationalDBModule
from flask_docker.server.routes.modules import modules_api
from flask_docker.services.database.relational_db import RelationalDB


def setup_relational_db(relational_db: RelationalDB):
    if is_development() or is_testing():
        relational_db.delete_models()
    relational_db.create_models()


def setup_logging(app: Flask):
    app.logger.disabled = not is_development()
    logging.getLogger("werkzeug").disabled = not is_development()
    logging.config.dictConfig(LOGGING_CONFIG)


def create_app(relational_db: RelationalDB) -> Flask:
    app = Flask(os.environ["SERVER_NAME"])
    CORS(app)
    RequestID(app)
    setup_logging(app)

    app.register_blueprint(modules_api, url_prefix="/modules")

    @app.after_request
    def after_request(response: Response) -> Response:
        message = "{} {} {} {} {} {}".format(
            current_request_id(),
            request.remote_addr,
            request.method,
            request.scheme,
            request.full_path,
            response.status,
        )
        logging.getLogger("flask_docker").info(message)
        response.headers.add("X-REQUEST-ID", current_request_id())
        return response

    @app.errorhandler(Exception)
    def handle_exception(e: Exception):
        error_handler = ErrorHandler()
        response = error_handler.handle(e)
        return response

    modules = [RelationalDBModule(relational_db)]
    FlaskInjector(app=app, modules=modules)

    setup_relational_db(relational_db)
    return app
