from sonarargs import parse_cli_args
import subprocess
import os
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

        # e.g. ee950 
        version = output.up
        # e.g. 9.5.0-enterprise
        tag = tags.get(version)
        # e.g. 950 - if statement to catch sq dn
        tag_num = version[len(version)-3:] 
        # e.g. 9950
        port = int('9' + tag_num)
        # e.g. '9.6', '10', '11', '12', '13', '14', '15' for pg, '2017', '2019' for ms, '18', '21' for or
        dbv = '13' if output.databaseversion is None else output.databaseversion[0]

        # # set database type 'pg', 'ms', or 'or' defaults to h2 if not set
        # db_type = 'h2' if output.database is None else output.database[0]
        db = 'h2' if output.database is None else output.database[0] + dbv

        loglevel = 'INFO' if output.verbose is False else 'DEBUG'

        myenv = {
            **os.environ,
            "BUILD": str(tag_num),
            "DOCKER_FULL_TAG": str(tag),
            "SQ_VERSION": str(version),
            "DB": str(db),
            "DB_VERSION": str(dbv),            
            "SONAR_LOG_LEVEL": str(loglevel)
        }

        # # enables the ability to spin up another instance of a different version to compare
        # # the compare docker-compose file is in another folder to avoid network names colliding (assigned according to parent folder)
        # docker_compose_file = './compare/docker-compose_script_compare.yml' if output.compare == True else './docker-compose_script.yml'
        docker_compose_file = './docker-compose_script.yml'

        # enables ability to add parameters for db options, version 1.28.0 or later of docker-compose is required for --profile
        profile = "--profile sqh2" if db == 'h2' else "--profile dbs --profile sqdb"

        # 'up' state has additional logging so user can see sonarqube instance status
        state = '--profile dbs --profile sqdb --profile sqh2 down' if output.dn == True else f"{profile} up -d" 
        #&& sleep 1 && docker context show && docker exec -it sqtool{tag_num} tail -f logs/sonar.log"

        process_cmd = f"docker-compose --file {docker_compose_file} {state}"
        print(process_cmd)
        process = subprocess.Popen(process_cmd, shell=True, env=myenv)

        process.wait()

if __name__ == "__main__":
    main()
