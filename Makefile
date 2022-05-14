SHELL := /bin/bash

install:
	poetry install

bump:
	poetry version prerelease

build:
	rm -rf dist
	poetry build

pipx:
	-pipx uninstall "$(shell poetry version | awk '{print $$1}')"
	pipx install --force "$(shell ls -d dist/*.whl)"

publish:
	poetry publish

clean:
	rm -rf venv
	rm -rf imports cdktf.out

init:
	terraform init

upgrade:
	terraform init -upgrade

validate:
	terraform validate

plan:
	terraform plan -out=.plan

apply:
	terraform apply .plan
	rm -f .plan

refresh:
	terraform refresh

console:
	terraform console

apply-refresh:
	terraform apply -refresh-only

get:
	poetry run cdktf get

synth:
	cdktf synth
