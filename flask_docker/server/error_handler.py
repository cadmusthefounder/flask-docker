import logging
from http import HTTPStatus
from typing import Tuple, Union

from flask_docker.common.exceptions import (
    InvalidRequestError,
    MessageException,
    ObjectAlreadyExistsError,
    ObjectNotFoundError,
    RelationalDBError,
    ValueError,
)


class ErrorHandler:
    ERROR_MAPPING = {
        ObjectNotFoundError.__name__: HTTPStatus.NOT_FOUND,
        ObjectAlreadyExistsError.__name__: HTTPStatus.CONFLICT,
        RelationalDBError.__name__: HTTPStatus.INTERNAL_SERVER_ERROR,
        InvalidRequestError.__name__: HTTPStatus.BAD_REQUEST,
        ValueError.__name__: HTTPStatus.INTERNAL_SERVER_ERROR,
    }

    def __init__(self):
        self._logger = logging.getLogger("flask_docker_logger")

    def handle(self, exception: Union[Exception, MessageException]) -> Tuple[dict, int]:
        class_name = type(exception).__name__
        if class_name in ErrorHandler.ERROR_MAPPING and isinstance(
            exception, MessageException
        ):
            http = ErrorHandler.ERROR_MAPPING[class_name]
        else:
            http = HTTPStatus.INTERNAL_SERVER_ERROR
            exception = MessageException("Something went wrong at the server.")

        error_response = self._make_error_response(http, exception)
        self._log_based_on_http(http, exception)
        return (error_response, http.value)

    def _log_based_on_http(self, http: HTTPStatus, exception: MessageException):
        class_name = type(exception).__name__
        log_message = "{} raised. Message: {} Messages: {}".format(
            class_name, exception.message, exception.messages
        )
        if http is HTTPStatus.INTERNAL_SERVER_ERROR:
            self._logger.error(exception, exc_info=True)
            self._logger.error(log_message)
        elif http is HTTPStatus.SERVICE_UNAVAILABLE:
            self._logger.warn(log_message)
        else:
            self._logger.info(log_message)

    def _make_error_response(
        self, http: HTTPStatus, exception: MessageException
    ) -> dict:
        error_response = {
            "error": {
                "type": http.phrase,
                "status": http.value,
                "message": exception.message,
                "messages": exception.messages,
            }
        }
        return error_response
