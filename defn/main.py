from amanibhavam import AwsOrganizationStack, NullStack
from cdktf import App, LocalBackend


def main():
    app = App()

    stack = AwsOrganizationStack(app, "kitt", "kitt", "defn.sh", "us-west-2")
    LocalBackend(stack, path="./terraform.tfstate")

    stack = AwsOrganizationStack(app, "katt", "katt", "defn.sh", "us-west-2")
    LocalBackend(stack, path="./terraform.tfstate")

    stack = NullStack(app, "example")
    LocalBackend(stack, path="./terraform.tfstate")

    app.synth()

if __name__ == '__main__':
    main()
