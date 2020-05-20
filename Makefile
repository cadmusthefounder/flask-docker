environment = $(shell test -e .env || cp sample.env .env; echo .env)
include $(environment)
export $(shell sed 's/=.*//' $(environment))

.DEFAULT_GOAL := help

## Don't worry! We've got you covered.
.PHONY: help
help:
	@printf "Usage\n";

	@awk '{ \
			if ($$0 ~ /^.PHONY: [a-zA-Z\-\_0-9]+$$/) { \
				helpCommand = substr($$0, index($$0, ":") + 2); \
				if (helpMessage) { \
					printf "\033[36m%-20s\033[0m %s\n", \
						helpCommand, helpMessage; \
					helpMessage = ""; \
				} \
			} else if ($$0 ~ /^[a-zA-Z\-\_0-9.]+:/) { \
				helpCommand = substr($$0, 0, index($$0, ":")); \
				if (helpMessage) { \
					printf "\033[36m%-20s\033[0m %s\n", \
						helpCommand, helpMessage; \
					helpMessage = ""; \
				} \
			} else if ($$0 ~ /^##/) { \
				if (helpMessage) { \
					helpMessage = helpMessage"\n                     "substr($$0, 3); \
				} else { \
					helpMessage = substr($$0, 3); \
				} \
			} else { \
				if (helpMessage) { \
					print "\n                     "helpMessage"\n" \
				} \
				helpMessage = ""; \
			} \
		}' \
		$(MAKEFILE_LIST)

## -- Deployment --

## Only builds image when ${DEVELOPMENT_ENVIRONMENT} is DEVELOPMENT.
##
.PHONY: build
build:
	@scripts/build.sh

## Deploy based on ${DEVELOPMENT_ENVIRONMENT} variable set in .env file.
##
## DEVELOPMENT:
##     1) Build govtext_auth's images.
##     2) Create a docker network if it doesn't exist.
##     3) Start containers in data tier.
##     4) Start containers in app tier with hot reloading.
##
.PHONY: up
up: build
	-@scripts/create-network.sh
	@scripts/up.sh -t all

## Deploy based on ${DEVELOPMENT_ENVIRONMENT} variable set in .env file.
##
## DEVELOPMENT:
##     1) Create a docker network if it doesn't exist.
##     2) Start containers in data tier.
##
.PHONY: up-data
up-data:
	-@scripts/create-network.sh
	@scripts/up.sh -t data

## Deploy based on ${DEVELOPMENT_ENVIRONMENT} variable set in .env file.
##
## DEVELOPMENT:
##     1) Build govtext_auth's images.
##     2) Start containers in app tier with hot reloading.
##
.PHONY: up-app
up-app: build
	@scripts/up.sh -t app

## Deploy based on ${DEVELOPMENT_ENVIRONMENT} variable set in .env file.
##
## DEVELOPMENT:
##     1) Stops all running containers in app tier.
##     2) Stops all running containers in db tier.
##     3) Destroy the docker network.
##
.PHONY: down
down:
	@scripts/down.sh -t all
	-@scripts/destroy-network.sh

## Deploy based on ${DEVELOPMENT_ENVIRONMENT} variable set in .env file.
##
## DEVELOPMENT:
##     1) Stops all running containers in db tier.
##     2) Destroy the docker network.
##
.PHONY: down-data
down-data:
	@scripts/down.sh -t data
	-@scripts/destroy-network.sh

## Deploy based on ${DEVELOPMENT_ENVIRONMENT} variable set in .env file.
##
## DEVELOPMENT:
##     1) Stops all running containers in app tier.
##
.PHONY: down-app
down-app:
	@scripts/down.sh -t app

## -- Utility --

## Recreate a fresh .env from sample.env
##
.PHONY: env
env:
	@rm .env
	@cp sample.env .env

## Run formatters and linters.
##
.PHONY: pre-commit
pre-commit:
	@poetry run pre-commit run --all-files

## Write commit messages.
##
.PHONY: commit
commit: pre-commit
	@npm run commit

## Remove __pycache__ folder and *.pyc files
##
.PHONY: clean
clean:
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete


## -- Dependency --

## List python dependencies. Defaults to current directory.
##
.PHONY: list
list:
	@poetry show --no-dev --tree

## Install project dependencies.
##
.PHONY: install
install:
	@npm install
	@poetry install
	@poetry run pre-commit install


## -- Test --

## Run unit tests.
##
.PHONY: unit
unit:
	@poetry run pytest tests/unit -v -s
