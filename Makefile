PWD=$(shell pwd)
.DEFAULT_GOAL := help

##  --------
##@ Database
##  --------

db-local-apply: .revolve-dep ## Apply database migrations scripts
	@python -m yoyo --config yoyo-local.ini apply
.PHONY: db-local-apply

db-local-reset: ## Fully reset local db (use Docker)
	@docker compose -f docker/docker-compose.yml down -v || true
	@docker volume rm astraeus-db || true
	@docker volume create astraeus-db
	@docker compose -f docker/docker-compose.yml up -d
	@sleep 5
	@make db-local-apply
.PHONY: db-local-reset

##  -------
##@ Install
##  -------

install-editable: ## Install local dev with editable option
	@echo "===> $@ <==="
	@rm -rf build dist
	@python -m build
	@pip install --force-reinstall --editable .
.PHONY: install-editable

install: ## Install application
	@echo "===> $@ <==="
	@rm -rf build dist
	@python -m build
	@pip install --force-reinstall .
.PHONY: install

install-test: install ## Install application and tests modules
	@echo "===> $@ <==="
	@pip install astraeus-common\[test\]
.PHONY: install-test

install-all: install install-test ## Install all application dependencies
	@echo "===> $@ <==="
	@pip install astraeus-common\[dev\]
.PHONY: install-all

build: install ## Build the application
	@python -m build

##  -------
##@ Quality
##  -------

apply-isort: ## Applying autosort of imports
	@echo "===> $@ <==="
	@if ! python -m isort > /dev/null; then $(MAKE) install-test; fi
	@python -m isort ./src ./test --sp .github/linters/.isort.cfg
	@echo "Done !"
.PHONY: apply-isort

check-linter: ## Run flake8 linter on sources
	@echo "===> $@ <==="
	@if ! python -m flake8 --version; then $(MAKE) install-test; fi
	@python -m flake8 --config .github/linters/.flake8 ./src ./test
	@echo "Done !"
.PHONY: check-linter

##  ----
##@ Misc
##  ----

prepare-release: ## Prepare files before making a new release of version
	@echo "===> $@ <==="
	@sed -Ei 's/version = .*/version = "${VERSION}"/g' pyproject.toml
.PHONY: prepare-release

.DEFAULT_GOAL := help
APPLICATION_TITLE := Astraeus - astraeus-common \n ================
.PHONY: help
# See https://www.thapaliya.com/en/writings/well-documented-makefiles/
help: ## Display this help
	@awk 'BEGIN {FS = ":.* ##"; printf "\n\033[32;1m ${APPLICATION_TITLE}\033[0m\n\n\033[1mUsage:\033[0m\n  \033[31mmake \033[36m<option>\033[0m\n"} /^[%a-zA-Z_-]+:.* ## / { printf "  \033[33m%-25s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' ${MAKEFILE_LIST}

##@
