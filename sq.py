import argparse
import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(
    prog='sq', 
    description='run any version or edition of SQ in a docker container')

# positional argument
my_parser.add_argument(
    'sqEditionVersion',
    metavar='sqEdVer',
    type=str,
    help='SQ edition and version e.g. ee899')

# optional arguments
my_parser.add_argument(
    '-vv',
    '--verbose',
    action='store_true',
    help='enable verbose output')

my_parser.add_argument(
    '-db',
    '--database',
    action='store',
    nargs=1,
    choices=['pg', 'ms', 'orc'],
    help='choose external database')

args = my_parser.parse_args()
print(args)
print(args.sqEditionVersion)
print(args.database)

