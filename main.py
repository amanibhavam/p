import foo.init

''' init must run before cdktf '''

from cdktf import App
from cdktf_cdktf_provider_null import Resource
from constructs import Construct

from foo.null import NullStack


def main():
    app = App()

    stack = NullStack(app, "demo")

    Resource(stack, "ex1")
    Resource(stack, "ex2")

    app.synth()

if __name__ == '__main__':
    main()
