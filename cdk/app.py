#!/usr/bin/env python3

from aws_cdk import (
    aws_ssm as ssm,
    core
)

from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')


class SSMParameterEnvAutomation(core.Stack):

    def __init__(self, scope: core.Stack, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.parameter = ssm.StringParameter(self, "test", string_value='TEST', parameter_name='TEST')
        
        for main_key in config:
            if 'DEFAULT' not in main_key:
                print("==> {}".format(main_key))
                for parameter in config[main_key]:
                    print("====> {}/{} == {}".format(main_key,parameter,config[main_key][parameter]))


for main_key in config:
    if 'DEFAULT' not in main_key:
        app = core.App()
        _env = core.Environment(account=config[main_key]['account_number'], region=config[main_key]['region'])
        SSMParameterEnvAutomation(app, "automation-env-vars-{}".format(config[main_key]['account_number'],config[main_key]['region']), env=_env)
    
app.synth()