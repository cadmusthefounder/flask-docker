from typing import Tuple
from uuid import UUID

from flask import Blueprint
from flask_injector import inject

from flask_docker.services.database.relational_db import RelationalDB

modules_api = Blueprint("modules_api", __name__)


@inject
@modules_api.route("/<module_id>", methods=["GET"])
def get_module(relational_db: RelationalDB, module_id: str) -> Tuple[dict, int]:
    module_uuid = UUID(module_id)
    module = relational_db.query_module(id=module_uuid)

    response = {"id": module.id, "code": module.code, "size": module.size}

    return (response, 200)
