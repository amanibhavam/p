from amanibhavam import AwsOrganizationStack, NullStack
from cdktf import App, LocalBackend, TerraformStack
from cdktf_cdktf_provider_digitalocean import DigitaloceanProvider, Project
from constructs import Construct


class DigitaloceanStack(TerraformStack):
    """cdktf Stack for Digital Ocean Kubernetes"""

    def __init__(self, scope: Construct, namespace: str, name: str):
        super().__init__(scope, namespace)

        DigitaloceanProvider(self, "digitalocean")

        Project(self, "project", name=name)

def main():
    app = App()

    stack = NullStack(app, "null")
    LocalBackend(stack, path="./terraform.tfstate")

    stack = AwsOrganizationStack(app, "kitt", "kitt", "defn.sh", "us-west-2")
    LocalBackend(stack, path="./terraform.tfstate")

    stack = AwsOrganizationStack(app, "katt", "katt", "defn.sh", "us-west-2")
    LocalBackend(stack, path="./terraform.tfstate")

    stack = DigitaloceanStack(app, "do", "defn")
    LocalBackend(stack, path="./terraform.tfstate")

    app.synth()

if __name__ == '__main__':
    main()
