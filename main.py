import foo.init

""" init must run before cdktf """

import typer
from cdktf import App
from cdktf_cdktf_provider_null import Resource

from foo.demo import DemoStack


def main(name: str = "demo"):
    app = App()

    stack = DemoStack(app, name)

    app.synth()


if __name__ == "__main__":
    typer.run(main)
