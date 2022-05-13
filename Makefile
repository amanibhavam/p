SHELL := /bin/bash

install:
	poetry install

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
