from typing import List, Optional, Union
from uuid import UUID

from sqlalchemy import create_engine, inspect
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import create_database, database_exists

from flask_docker.common.exceptions import (
    ObjectAlreadyExistsError,
    ObjectNotFoundError,
    RelationalDBError,
    ValueError,
)
from flask_docker.common.helper import get_current_utc_time
from flask_docker.services.database.models import Base, Module


class RelationalDB:
    def __init__(self, connection_url: str):
        if not database_exists(connection_url):
            create_database(connection_url)

        self._connection_url = connection_url
        self._engine = create_engine(self._connection_url)
        self._Session = scoped_session(sessionmaker(bind=self._engine))

    @property
    def connection_url(self) -> str:
        return self._connection_url

    @property
    def tablecodes(self) -> List[str]:
        inspector = inspect(self._engine)
        return inspector.get_table_codes()

    @staticmethod
    def make_postgresql_connection_url(
        host: str, port: str, user: str, password: str, db: str
    ) -> str:
        return "postgresql://{}:{}@{}:{}/{}".format(user, password, host, port, db)

    def commit(self):
        try:
            self._Session.commit()
        except Exception as e:
            self._Session.rollback()
            raise e

    def create_models(self):
        Base.metadata.create_all(bind=self._engine)

    def delete_models(self):
        Base.metadata.drop_all(bind=self._engine)

    def has_table(self, tablecode: str) -> bool:
        return tablecode in self.tablecodes

    def __enter__(self):
        self._Session()

    def __exit__(self, exception_type, exception_value, traceback):
        self._Session.rollback()
        self._Session.remove()
        if exception_value:
            raise exception_value

    ########################
    # Module
    ########################

    def query_module(
        self,
        id: Optional[UUID] = None,
        code: Optional[str] = None,
        update: bool = False,
    ) -> Module:
        if all(v is None for v in [id, code]):
            raise ValueError("Either `id` or `code` must be specified.")

        try:
            query = (
                self._Session.query(Module).with_for_update()
                if update
                else self._Session.query(Module)
            )
            if id:
                module = query.get(id)
            else:
                module = query.filter(Module.code == code).first()

            if not module:
                raise ObjectNotFoundError("No such module.")
        except SQLAlchemyError:
            raise RelationalDBError(
                "Unexpected error has occured while querying module."
            )
        return module

    def insert_module(self, data: dict) -> Module:
        try:
            module = Module(**data)
            self._Session.add(module)
            self.commit()
        except IntegrityError:
            raise ObjectAlreadyExistsError("Module already exists.")
        except SQLAlchemyError:
            raise RelationalDBError(
                "Unexpected error has occured while creating module."
            )
        return module

    def update_module(self, data: Union[dict, Module]) -> Module:
        try:
            if isinstance(data, dict):
                module = self.query_module(
                    id=data.get("id", None), code=data.get("code", None), update=True
                )
                for k, v in data.items():
                    setattr(module, k, v)
            else:
                module = data
            module.updated_at = get_current_utc_time()
            self.commit()
        except IntegrityError:
            raise ObjectAlreadyExistsError("Invalid update of module information.")
        except SQLAlchemyError:
            raise RelationalDBError(
                "Unexpected error has occured while updating module."
            )
        return module

    def delete_module(
        self, id: Optional[UUID] = None, code: Optional[str] = None
    ) -> Module:
        try:
            module = self.query_module(id=id, code=code)
            self._Session.delete(module)
            self.commit()
        except SQLAlchemyError:
            raise RelationalDBError(
                "Unexpected error has occured while deleting module."
            )
        return module
