#!/usr/bin/env bash

while getopts ":t:" opt; do
  case $opt in
    t)
      TIER=$OPTARG
      echo "-t was triggered, Tier: $OPTARG" >&2
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

if [ "$ENVIRONMENT" == "DEVELOPMENT" ] || [ "$ENVIRONMENT" == "TESTING" ]
then
  if [ "$TIER" == "data" ]
  then
    docker-compose -p govtext -f docker-compose.data.yml up;
  elif [ "$TIER" == "app" ]
  then
    docker-compose -p govtext -f docker-compose.development.yml up;
  elif [ "$TIER" == "all" ]
  then
    docker-compose -p govtext -f docker-compose.data.yml -f docker-compose.development.yml up;
  fi
elif [ "$ENVIRONMENT" == "STAGING" ]
then
  docker stack deploy -c docker-compose.staging.yml $DOCKER_STACK_NAME;
elif [ "$ENVIRONMENT" == "PRODUCTION" ]
then
  docker stack deploy -c docker-compose.production.yml $DOCKER_STACK_NAME;
fi
