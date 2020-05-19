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
