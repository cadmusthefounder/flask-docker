from flask_log_request_id import RequestIDLogFilter

########################
# Logging
########################

LOGGING_CONFIG: dict = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(levelname)s - %(processName)s:%(process)d - %(threadName)s - %(filename)s:%(funcName)s:%(lineno)s - %(message)s"
        }
    },
    "filters": {"request_id_log_filter": {"()": RequestIDLogFilter}},
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
            "filters": ["request_id_log_filter"],
        }
    },
    "loggers": {"flask_docker_logger": {},},
    "root": {"level": "DEBUG", "handlers": ["console"]},
}
