SHELL := /bin/bash

typecheck:
	. ./venv/bin/activate && mypy main.py

main.tf.json: cdktf.out/stacks/default/cdk.tf.json
	cat $< | jq 'walk(if type == "object" then if .["//"] == null then . else del(.["//"]) end else . end)' > $@.1
	mv -f $@.1 $@

install: venv/bin/activate
	$(MAKE) cdktf-nodejs
	$(MAKE) cdktf-python

clean:
	rm -rf venv
	rm -rf node_modules
	rm -rf imports cdktf.out

venv/bin/activate:
	$(MAKE) cdktf-python

cdktf-nodejs:
	npm install -g npm
	npm install

cdktf-python:
	python -m venv venv
	. venv/bin/activate && python -m pip install --upgrade pip
	. venv/bin/activate && python -m pip install -r requirements.txt

check:
	flake8 $(shell git ls-files | grep 'py$$')

init:
	terraform init

upgrade:
	terraform init -upgrade

fmt:
	for a in *.tf *.tfvars; do if [[ -f $$a ]]; then terraform fmt $$a; fi; done
	black --quiet -c pyproject.toml $(shell git ls-files | grep 'py$$')
	isort --quiet $(shell git ls-files | grep 'py$$')
	git diff

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

apply-refresh: cdk.tf.json
	terraform apply -refresh-only

get:
	./node_modules/.bin/cdktf get

build:
	. ./venv/bin/activate && ./node_modules/.bin/cdktf synth
	$(MAKE) main.tf.json

fix:
	pre-commit run -a
