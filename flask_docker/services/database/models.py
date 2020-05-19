import uuid

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import UUIDType

from flask_docker.common.helper import get_current_utc_time

Base = declarative_base()


class Module(Base):
    __tablename__ = "modules"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    code = Column(String, unique=True, nullable=False)
    size = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=get_current_utc_time)
    updated_at = Column(DateTime, nullable=False, default=get_current_utc_time)
