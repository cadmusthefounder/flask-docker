import os
from typing import Generator

import pytest
from flask import Flask
from flask.testing import FlaskClient

from flask_docker.server.app import create_app
from flask_docker.services.database.relational_db import RelationalDB


@pytest.fixture
def relational_db():
    relational_db_connection_url = RelationalDB.make_postgresql_connection_url(
        host=os.environ["RELATIONAL_DB_NAME"],
        port=os.environ["RELATIONAL_DB_PORT"],
        user=os.environ["RELATIONAL_DB_USERNAME"],
        password=os.environ["RELATIONAL_DB_PASSWORD"],
        db=os.environ["RELATIONAL_DB_DB"],
    )

    relational_db = RelationalDB(relational_db_connection_url)

    with relational_db:
        yield relational_db


@pytest.fixture
def app(relational_db: RelationalDB,) -> Flask:

    application = create_app(relational_db=relational_db,)
    application.testing = True
    return application


@pytest.fixture
def client(app: Flask) -> Generator[FlaskClient, None, None]:
    with app.test_client() as client:
        yield client
