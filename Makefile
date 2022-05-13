SHELL := /bin/bash

install: venv/bin/activate
	@true

clean:
	rm -rf venv
	rm -rf imports cdktf.out

venv/bin/activate:
	python -m venv venv
	./venv/bin/python -m pip install --upgrade pip
	./venv/bin/python -m pip install -r requirements.txt

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
	cdktf get

synth:
	cdktf synth
