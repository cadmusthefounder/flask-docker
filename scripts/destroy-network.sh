#!/usr/bin/env bash

docker network remove $DOCKER_NETWORK \
    || >&2 echo "Failed to remove Docker network!"
