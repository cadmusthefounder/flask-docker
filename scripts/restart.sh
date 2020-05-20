#!/usr/bin/env bash

if [ "$ENVIRONMENT" == "DEVELOPMENT" ]
then
    docker-compose -f docker-compose.development.yml restart ;
elif [ "$ENVIRONMENT" == "STAGING" ]
then
    docker stack deploy -c docker-compose.staging.yml $DOCKER_STACK_NAME;
elif [ "$ENVIRONMENT" == "PRODUCTION" ]
then
    docker stack deploy -c docker-compose.production.yml $DOCKER_STACK_NAME;
fi
