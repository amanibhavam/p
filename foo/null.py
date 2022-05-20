from cdktf import NamedRemoteWorkspace, RemoteBackend, TerraformStack
from cdktf_cdktf_provider_github import GithubProvider
from cdktf_cdktf_provider_null import NullProvider
from cdktf_cdktf_provider_tfe import TfeProvider
from constructs import Construct
from defn_cdktf_provider_buildkite.buildkite import BuildkiteProvider
from defn_cdktf_provider_cloudflare.cloudflare import CloudflareProvider


class NullStack(TerraformStack):
    """cdktf Stack for an example"""

    def __init__(self, scope: Construct, namespace: str):
        super().__init__(scope, namespace)

        NullProvider(self, "null")
        BuildkiteProvider(self, "buildkite", organization="defn", api_token="")
        TfeProvider(self, "tfe")
        GithubProvider(self, "github", organization="defn")
        CloudflareProvider(self, "cloudflare")

        w = NamedRemoteWorkspace(name="bootstrap")
        RemoteBackend(self, organization="defn", workspaces=w)
