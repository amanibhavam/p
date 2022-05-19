SHELL := /bin/bash

plan:
	time e +plan --stack=demo

apply:
	time e +apply --stack=demo
