#!/usr/bin/env python3

from aws_cdk import (
    aws_ssm as ssm,
    core
)

from configparser import ConfigParser
from os import getenv

config = ConfigParser()
config.read('config.ini')


class SSMParameterEnvAutomation(core.Stack):

    def __init__(self, scope: core.Stack, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        
        count = 0
        for parameter in config[my_env]:
            
            parameter_name = "/{}/{}".format(my_env, parameter)
            parameter_value = config[my_env][parameter]
            
            self.parameter = ssm.StringParameter(
                self, "Parameter{}".format(count),
                string_value=parameter_value, 
                parameter_name=parameter_name
            )
            
            count += 1


my_env = getenv('MY_ENV')
app = core.App()
_env = core.Environment(account=config[my_env]['account_number'], region=config[my_env]['region'])
SSMParameterEnvAutomation(app, "automation-env-vars-{}".format(config[my_env]['account_number'],config[my_env]['region']), env=_env)
    
app.synth()