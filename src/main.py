import json
import os

context = {
    "excludeStackIdFromLogicalIds": True,
    "allowSepCharsInLogicalIds": True
}
os.environ.setdefault("CDKTF_CONTEXT_JSON", json.dumps(context))

from cdktf import App
from cdktf_cdktf_provider_null import Resource
from constructs import Construct

from foo.null import NullStack


def main():
    app = App()

    stack = NullStack(app, "demo")

    Resource(stack, "ex1")

    app.synth()

if __name__ == '__main__':
    main()
