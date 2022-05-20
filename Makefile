plan:
	earthly +plan --stack=demo

apply:
	earthly --push +apply --stack=demo
