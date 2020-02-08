#!/usr/bin/env python

import sys, configparser

config = configparser.ConfigParser()
config.read_file(sys.stdin)

for sec in config.sections():
    print(sec)
