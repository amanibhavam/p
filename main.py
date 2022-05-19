from amanibhavam import NullStack
from cdktf import App, LocalBackend, TerraformStack
from cdktf_cdktf_provider_null import Resource
from constructs import Construct
from defn_cdktf_provider_buildkite.buildkite import BuildkiteProvider


class BuildkiteStack(TerraformStack):
    """cdktf Stack for Buildkite pipeline"""

    def __init__(self, scope: Construct, namespace: str):
        super().__init__(scope, namespace)

        BuildkiteProvider(self, "buildkite", organization="defn", api_token="")

def main():
    app = App()

    stack = NullStack(app, "demo")
    Resource(stack, "ex3")
    Resource(stack, "ex4")
    Resource(stack, "ex5")
    Resource(stack, "ex6")
    Resource(stack, "ex7")

    BuildkiteProvider(stack, "buildkite", organization="defn", api_token="")

    LocalBackend(stack, path="./terraform.tfstate")


    app.synth()

if __name__ == '__main__':
    main()
