SHELL := /bin/bash

bump:
	poetry version prerelease

build:
	rm -rf dist
	poetry build

install:
	-pipx uninstall "$(shell poetry version | awk '{print $$1}')"
	pipx install --force "$(shell ls -d dist/*.whl)"

publish:
	poetry publish
