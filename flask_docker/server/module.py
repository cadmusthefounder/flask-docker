from typing import Generator

from flask_injector import Binder, Module, request

from flask_docker.services.database.relational_db import RelationalDB


class RelationalDBModule(Module):
    def __init__(self, relational_db: RelationalDB):
        self._relational_db = relational_db

    def configure(self, binder: Binder):
        binder.bind(RelationalDB, to=next(self.relational_db), scope=request)

    @property
    def relational_db(self) -> Generator[RelationalDB, None, None]:
        with self._relational_db:
            yield self._relational_db
