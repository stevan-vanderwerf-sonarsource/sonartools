from sonarargs import parse_cli_args
import subprocess
import os
import socket
import json
import sonartagfetch as dr
import sonartagprocess

def main():
    """Parses user input and passes those values to the Container object"""

    output = parse_cli_args()
    print(output)

    if output.up or output.dn:
        # updates docker tags, should only take < 1 second)
        dr.update_tags()
        sonartagprocess.update_dictionary()

        # loads the docker tags data as a dictionary
        with open('sonartagdictionary.json') as f:
            data = f.read()
        tags = json.loads(data)

        # e.g. ee950 - if statement to catch sq dn
        version = output.up
        # e.g. 9.5.0-enterprise
        tag = tags.get(version)
        # e.g. 950 - if statement to catch sq dn
        tag_num = version[len(version)-3:] #if output.up else '000'
        # e.g. 9950
        port = int('9' + tag_num)
        # e.g. '9.6', '10', '11', '12', '13', '14', '15' for pg, '2017', '2019' for ms, '18', '21' for or
        dbv = '13' if output.databaseversion is None else output.databaseversion[0]

        # set database type 'pg', 'ms', or 'or' defaults to h2 if not set
        db_type = 'h2' if output.database is None else output.database[0]

        # checks if port is free
        port_free = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex(('localhost', port)) == 0

        myenv = {
            **os.environ,
            "BUILD": str(tag_num),
            "SQ_VERSION": str(tag),
            "DB": str(db_type),
            "SONAR_JDBC_USERNAME": str('sonar'),
            "SONAR_JDBC_PASSWORD": str('sonar'),
            "SONAR_JDBC_URL": str('jdbc:postgresql://db:5432/sonardb'),
            "SONAR_LOG_LEVEL": str('DEBUG'),
            "DB_VERSION": str(dbv)
        }

        # enables the ability to spin up another instance of a different version to compare
        # the compare docker-compose file is in another folder to avoid network names colliding (assigned according to parent folder)
        docker_compose_file = '~/code/tools/compare/docker-compose_script_compare.yml' if output.compare == True else '~/code/tools/docker-compose_script.yml'

        # enables ability to add parameters for db options, version 1.28.0 or later of docker-compose is required for --profile
        profile = "--profile sqh2" if db_type == 'h2' else "--profile dbs --profile sqdb"

        # 'up' state has additional logging so user can see sonarqube instance status
        state = 'down' if output.dn == True else f"up -d && sleep 5 && docker exec -it sq{tag_num} tail -f logs/sonar.log"

        process_cmd = f"docker-compose --file {docker_compose_file} {profile} {state}"
        print(process_cmd)
        process = subprocess.Popen(process_cmd, shell=True, env=myenv)

        process.wait()

if __name__ == "__main__":
    main()
