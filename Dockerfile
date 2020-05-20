########################
# Base Image
########################

FROM python:3.7-slim as base-image

ARG SERVER_PORT
ARG WORKDIR_PATH
ARG VENV_PATH

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=$WORKDIR_PATH \
    SERVER_PORT=$SERVER_PORT \
    WORKDIR_PATH=$WORKDIR_PATH \
    VENV_PATH=$VENV_PATH

########################
# Build Image
########################

FROM base-image as build-image

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && python3 -m venv $VENV_PATH \
    && $VENV_PATH/bin/pip3 install --no-cache-dir --upgrade pip

WORKDIR $WORKDIR_PATH
COPY poetry.lock pyproject.toml ./

RUN pip3 install poetry \
    && poetry export -f requirements.txt > requirements.txt \
    && $VENV_PATH/bin/pip3 install -r requirements.txt

########################
# Runtime Image
########################

FROM base-image as runtime-image

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR $WORKDIR_PATH
COPY flask_docker/ flask_docker/
COPY tests/ tests/
COPY scripts/wait-for-it.sh wait-for-it.sh
COPY scripts/start.sh start.sh
COPY --from=build-image $WORKDIR_PATH/requirements.txt $WORKDIR_PATH/requirements.txt

COPY --from=build-image $VENV_PATH $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

RUN groupadd -r govtext && useradd -r -s /bin/false -g govtext govtext \
    && chown -R govtext:govtext $WORKDIR_PATH
USER govtext

EXPOSE $SERVER_PORT
