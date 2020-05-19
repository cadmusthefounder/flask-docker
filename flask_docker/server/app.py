import os

from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector

from flask_docker.server.module import RelationalDBModule
from flask_docker.server.routes.modules import modules_api
from flask_docker.services.database.relational_db import RelationalDB


def create_app(relational_db: RelationalDB) -> Flask:
    app = Flask(os.environ["SERVER_NAME"])
    CORS(app)

    app.register_blueprint(modules_api, url_prefix="/modules")

    modules = [RelationalDBModule(relational_db)]
    FlaskInjector(app=app, modules=modules)
    return app
