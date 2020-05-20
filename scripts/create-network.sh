#!/usr/bin/env bash

if [ "$ENVIRONMENT" == "DEVELOPMENT" ] || [ "$ENVIRONMENT" == "TESTING" ]
then
    docker network create -d bridge $DOCKER_NETWORK
else
    docker network create -d overlay --attachable --scope=swarm $DOCKER_NETWORK
fi
