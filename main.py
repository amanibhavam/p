#!/usr/bin/env python

from cdktf import App, TerraformStack
from constructs import Construct

from fogg.aws import Organization
from imports.aws import AwsProvider

account = "katt"
domain = "defn.sh"
account_names = (
    "org",
    "net",
    "log",
    "lib",
    "ops",
    "sec",
    "hub",
    "pub",
    "dev",
    "dmz",
)


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, "aws", region="us-west-2")

        Organization(self, account, domain, account_names)


app = App()
MyStack(app, "default")

app.synth()
