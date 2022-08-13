import argparse
import os
import sys

def parse_cli_args():
    
    my_parser = argparse.ArgumentParser(
        prog='sq', 
        description='run any version or edition of SQ in a docker container')

    # positional argument
    my_parser.add_argument(
        '-up',
        type=str,
        help='SQ edition and version e.g. ee899')

    my_parser.add_argument(
        '-dn',
        action='store_true',
        help='docker-compose down')

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
    return args

# print(args)
# print(args.up)
# print(args.database)

