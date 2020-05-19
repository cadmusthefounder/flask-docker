class MessageException(Exception):
    def __init__(self, message: str, messages: dict = {}):
        super().__init__(message)
        self._message = message
        self._messages = messages

    @property
    def message(self) -> str:
        return self._message

    @property
    def messages(self) -> dict:
        return self._messages


########################
# Relational DB
########################


class ObjectNotFoundError(MessageException):
    pass


class ObjectAlreadyExistsError(MessageException):
    pass


class RelationalDBError(MessageException):
    pass


########################
# Others
########################


class ValueError(MessageException):
    pass
