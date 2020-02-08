#!/usr/bin/env python3

import boto3
import os
from configparser import ConfigParser
from sys import argv

config = ConfigParser()
config.read('config.ini')

deploy_env = argv[1]

client = boto3.client('sts')
response = client.assume_role(RoleArn=config[deploy_env]['cross_account_role_arn'], RoleSessionName='test')

print('export MY_ENV={}'.format(deploy_env))
print('export AWS_ACCESS_KEY_ID={}'.format(response['Credentials']['AccessKeyId']))
print('export AWS_SECRET_ACCESS_KEY={}'.format(response['Credentials']['SecretAccessKey']))
print('export AWS_SESSION_TOKEN={}'.format(response['Credentials']['SessionToken']))
