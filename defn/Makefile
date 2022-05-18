SHELL := /bin/bash

gen:
	earthly --push +synth

plan:
	earthly --ci --output +plan --stack=${stack}

apply:
	earthly --push --ci --output +apply --stack=${stack}
