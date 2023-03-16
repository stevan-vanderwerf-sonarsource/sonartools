import argparse

def parse_cli_args():
    
    my_parser = argparse.ArgumentParser(
        prog='sq', 
        add_help=False,
        description='run any version or edition of SQ in a docker container')

    # positional arguments
    my_parser.add_argument(
        '-up',
        type=str,
        default='ee950', # needs to be set to force value for -up when -dn is called
        help='SQ edition and version e.g. ee899')

    my_parser.add_argument(
        '-dn',
        action='store_true',
        help='docker-compose down')

    # optional arguments
    my_parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='enable sonarqube startup verbose debug output')

    my_parser.add_argument(
        '-db',
        '--database',
        action='store',
        nargs=1,
        choices=['pg', 'ms', 'or'],
        help='choose external database')

    my_parser.add_argument(
        '-dbv',
        '--databaseversion',
        action='store',
        nargs=1,
        choices=['9.6', '10', '11', '12', '13', '14', '15', '2017', '2019', '18', '21'],
        help='choose external database version')


    my_parser.add_argument(
        '-c',
        '--compare',
        action='store_true',
        help='runs a second instance of SQ beside and existing one')   

    my_parser.add_argument(
        '-h',
        '--help',
        action='help',
        default=argparse.SUPPRESS,
        help='run any version or edition of dockerhub official images of sonarqube in a docker container')       

    args = my_parser.parse_args()
    return args
