import foo.init

''' init must run before cdktf '''

from cdktf import App
from cdktf_cdktf_provider_null import Resource

from foo.demo import DemoStack


def main():
    app = App()

    stack = DemoStack(app, "demo")

    app.synth()

if __name__ == '__main__':
    main()
