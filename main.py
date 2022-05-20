import foo.init

''' init must run before cdktf '''

from cdktf import App
from cdktf_cdktf_provider_null import Resource

from foo.null import NullStack


def main():
    app = App()

    stack = NullStack(app, "demo")

    app.synth()

if __name__ == '__main__':
    main()
