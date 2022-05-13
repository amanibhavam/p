SHELL := /bin/bash

main.tf.json: cdktf.out/stacks/default/cdk.tf.json
	cp $< $@

install: venv/bin/activate
	$(MAKE) cdktf-python
	$(MAKE) get

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

apply-refresh: cdk.tf.json
	terraform apply -refresh-only

get:
	cdktf get

build:
	. ./venv/bin/activate && cdktf synth
	$(MAKE) main.tf.json
