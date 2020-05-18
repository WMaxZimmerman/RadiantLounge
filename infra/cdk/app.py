#!/usr/bin/env python3

from aws_cdk import core

from stacks.personal_site_stack import PersonalSiteStack

account_number = os.environ['ACCOUNT_NUMBER']

app = core.App()
env = core.Environment(region="us-east-1", account=account_number)
PersonalSiteStack(app, "radiant-lounge-stack", env=env)

app.synth()
