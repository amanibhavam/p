from amanibhavam import NullStack
from cdktf import App, LocalBackend, TerraformStack
from constructs import Construct


def main():
    app = App()

    stack = NullStack(app, "null")
    LocalBackend(stack, path="./terraform.tfstate")

    app.synth()

if __name__ == '__main__':
    main()
