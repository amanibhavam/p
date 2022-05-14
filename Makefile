SHELL := /bin/bash

install:
	poetry install

bump:
	poetry version prerelease

build:
	poetry build -f wheel

publish:
	poetry publish
