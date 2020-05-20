#!/usr/bin/env bash

if [ "$ENVIRONMENT" == "DEVELOPMENT" ] || [ "$ENVIRONMENT" == "TESTING" ]
then
    docker-compose -f docker-compose.development.yml build;
fi
