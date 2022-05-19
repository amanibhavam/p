SHELL := /bin/bash

plan:
	time e +plan --stack=null

apply:
	time e +apply --stack=null
