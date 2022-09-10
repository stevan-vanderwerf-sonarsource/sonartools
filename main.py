from sq import parse_cli_args
import subprocess
import os
import sys
import socket


def main():
    """Parses user input and passes those values to the Container object"""

    # from https://github.com/axil/docker-registry-list
    tags = {
	"ce793":"7.9.3-community",
        "ee950":"9.5.0-enterprise",
        "ee899":"8.9.9-enterprise"
    }

    output = parse_cli_args()
    print(output)

    # e.g. ee950 - if statement to catch sq dn
    version = output.up #if output.up else ''
    # e.g. 9.5.0-enterprise
    tag = tags.get(version)
    # e.g. 950 - if statement to catch sq dn
    tag_num = version[len(version)-3:] #if output.up else '000'
    # e.g. 9950
    port = int('9' + tag_num)

    # set database type, defaults to h2 if not set
    db_type = 'h2' if output.database is None else output.database

    # checks if port is free
    port_free = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex(('localhost', port)) == 0

    myenvh2 = {
        **os.environ,
        "BUILD": str(tag_num),
        "SQ_VERSION": str(tag),
        "DB": str(db_type)
    }

    myenvdb = {
        **os.environ,
        "BUILD": str(tag_num),
        "SQ_VERSION": str(tag),
        "DB": str(db_type),
        "SONAR_JDBC_USERNAME": str('sonar'),
        "SONAR_JDBC_PASSWORD": str('sonar'),
        "SONAR_JDBC_URL": str('jdbc:postgresql://db:5432/sonardb')
    }
    # picks the right env variables based on database
    myenv = myenvh2 if db_type == 'h2' else myenvdb

    # enables the ability to spin up another instance of a different version to compare
    # the compare docker-compose file is in another folder to avoid network names colliding (assigned according to parent folder)
    docker_compose_file = 'compare/docker-compose_script_compare.yml' if output.compare == True else 'docker-compose_script.yml'

    # enables ability to add parameters for db options, version 1.28.0 or later of docker-compose is required for --profile
    profile = "" if db_type == 'h2' else "--profile dbs"

    state = 'down' if output.dn == True else 'up -d'
    print(state)

    process_cmd = f"docker-compose --file ./{docker_compose_file} --verbose {profile} {state}"
    print(process_cmd)
    process = subprocess.Popen(process_cmd, shell=True, env=myenv)

    process.wait()

if __name__ == "__main__":
    main()
