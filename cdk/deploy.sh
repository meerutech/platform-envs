#!/bin/bash

# Iterating through config.ini and passing in top level env values to use to create for each environment
for x in $(cat config.ini |./ini2arr.py);do 
  eval $(./source_aws_env.py $x)
  cdk diff
done

