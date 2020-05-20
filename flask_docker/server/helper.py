from flask import request

from flask_docker.common.exceptions import InvalidRequestError


def get_json_request_body() -> dict:
    if not request.is_json:
        raise InvalidRequestError("Expected JSON request.")

    data = request.get_json(silent=True)
    if not data:
        raise InvalidRequestError("Request body is not valid JSON.")
    return data
