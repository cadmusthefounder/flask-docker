import os
from datetime import datetime

import pytz

from flask_docker.common.constants import Environment


def get_current_utc_time() -> datetime:
    return pytz.utc.localize(datetime.utcnow())


def is_development() -> bool:
    return Environment(os.environ["ENVIRONMENT"]) is Environment.DEVELOPMENT


def is_testing() -> bool:
    return Environment(os.environ["ENVIRONMENT"]) is Environment.TESTING
