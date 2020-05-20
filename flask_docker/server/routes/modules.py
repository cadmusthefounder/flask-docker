from typing import Tuple
from uuid import UUID

from flask import Blueprint
from flask_injector import inject

from flask_docker.common.exceptions import InvalidRequestError
from flask_docker.server.helper import get_json_request_body
from flask_docker.services.database.relational_db import RelationalDB

modules_api = Blueprint("modules_api", __name__)


@inject
@modules_api.route("/<module_id>", methods=["GET"])
def get_module(relational_db: RelationalDB, module_id: str) -> Tuple[dict, int]:
    try:
        module_uuid = UUID(module_id)
    except ValueError:
        raise InvalidRequestError("Expect UUID.")
    module = relational_db.query_module(id=module_uuid)
    response = {
        "id": module.id,
        "code": module.code,
        "size": module.size,
        "created_at": module.created_at,
        "updated_at": module.updated_at,
    }
    return ({"module": response}, 200)


@inject
@modules_api.route("/", methods=["POST"])
def post_module(relational_db: RelationalDB) -> Tuple[dict, int]:
    data = get_json_request_body()
    module = relational_db.insert_module(data["module"])
    response = {
        "id": module.id,
        "code": module.code,
        "size": module.size,
        "created_at": module.created_at,
        "updated_at": module.updated_at,
    }
    return ({"module": response}, 201)


@inject
@modules_api.route("/", methods=["PUT"])
def put_module(relational_db: RelationalDB) -> Tuple[dict, int]:
    data = get_json_request_body()
    module = relational_db.update_module(data["module"])
    response = {
        "id": module.id,
        "code": module.code,
        "size": module.size,
        "created_at": module.created_at,
        "updated_at": module.updated_at,
    }
    return ({"module": response}, 200)


@inject
@modules_api.route("/<module_id>", methods=["DELETE"])
def delete_module(relational_db: RelationalDB, module_id: str) -> Tuple[dict, int]:
    try:
        module_uuid = UUID(module_id)
    except ValueError:
        raise InvalidRequestError("Expect UUID.")
    module = relational_db.delete_module(id=module_uuid)
    response = {
        "id": module.id,
        "code": module.code,
        "size": module.size,
        "created_at": module.created_at,
        "updated_at": module.updated_at,
    }
    return ({"module": response}, 200)
