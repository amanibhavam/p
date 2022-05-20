from amanibhavam import NullStack
from cdktf import App, RemoteBackend, TerraformStack
from cdktf_cdktf_provider_null import Resource
from cdktf_cdktf_provider_tfe import TfeProvider
from constructs import Construct
from defn_cdktf_provider_buildkite.buildkite import BuildkiteProvider


def main():
    app = App()

    stack = NullStack(app, "demo")
    Resource(stack, "ex3")
    Resource(stack, "ex4")
    Resource(stack, "ex5")
    Resource(stack, "ex6")
    Resource(stack, "ex7")

    BuildkiteProvider(stack, "buildkite", organization="defn", api_token="")

    RemoteBackend(stack, organization="defn", workspaces="bootstrap")


    app.synth()

if __name__ == '__main__':
    main()
