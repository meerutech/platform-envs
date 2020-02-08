#!/bin/bash

eval $(./source_aws_env.py)

cdk deploy
