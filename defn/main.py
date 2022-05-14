from amanibhavam import AwsOrganizationStack
from cdktf import App


def main():
    app = App()

    AwsOrganizationStack(app, "kitt", "kitt", "defn.sh", "us-west-2")
    AwsOrganizationStack(app, "katt", "katt", "defn.sh", "us-west-2")

    app.synth()

if __name__ == '__main__':
    main()
