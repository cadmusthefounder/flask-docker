import os

from flask_docker.common.helper import is_development
from flask_docker.server.app import create_app
from flask_docker.services.database.relational_db import RelationalDB

relational_db_connection_url = RelationalDB.make_postgresql_connection_url(
    host=os.environ["RELATIONAL_DB_NAME"],
    port=os.environ["RELATIONAL_DB_PORT"],
    user=os.environ["RELATIONAL_DB_USERNAME"],
    password=os.environ["RELATIONAL_DB_PASSWORD"],
    db=os.environ["RELATIONAL_DB_DB"],
)

relational_db = RelationalDB(relational_db_connection_url)

app = create_app(relational_db=relational_db)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ["SERVER_PORT"], debug=is_development())
