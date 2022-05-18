from amanibhavam import NullStack
from cdktf import App, LocalBackend, TerraformStack
from constructs import Construct
from cdktf_cdktf_provider_null import Resource


def main():
    app = App()

    stack = NullStack(app, "null")
    Resource(stack, "ex3")
    Resource(stack, "ex4")
    Resource(stack, "ex5")
    Resource(stack, "ex6")
    LocalBackend(stack, path="./terraform.tfstate")

    app.synth()

if __name__ == '__main__':
    main()
