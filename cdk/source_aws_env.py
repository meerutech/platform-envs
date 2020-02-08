#!/usr/bin/env python3

import boto3
import os
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

client = boto3.client('sts')
response = client.assume_role(RoleArn=config['test']['cross_account_role_arn'], RoleSessionName='test')
print('export AWS_ACCESS_KEY_ID={}'.format(response['Credentials']['AccessKeyId']))
print('export AWS_SECRET_ACCESS_KEY={}'.format(response['Credentials']['SecretAccessKey']))
print('export AWS_SESSION_TOKEN={}'.format(response['Credentials']['SessionToken']))
