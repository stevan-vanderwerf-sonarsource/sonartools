# Import the argparse library
import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(
    prog='sq', 
    description='run any version or edition of SQ in a docker container')

# Add the arguments
my_parser.add_argument(
    'sqEditionVersion',
    metavar='sqEdVer',
    type=str,
    help='SQ edition and version e.g. ee899')

args = my_parser.parse_args()
print(args)
print(args.sqEditionVersion)