import subprocess
import os
import sys
import json

# from https://github.com/axil/docker-registry-list
# tags = {
#     "ee950":"9.5.0-enterprise",
#     "ee899":"8.9.9-enterprise"
# }

with open('sqtagdictionary.json') as f:
    data = f.read()
# reconstructing the data as a dictionary
tags = json.loads(data)
print(tags)

# e.g. ee950
version = sys.argv[1]
# e.g. 9.5.0-enterprise
tag = tags.get(version)
# e.g. 950
tag_num = version[len(version)-3:]

# set database type, defaults to h2 if not set
db_type = 'h2' if len(sys.argv) < 3 else sys.argv[2]
print(db_type)

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
compare = False
docker_compose_file = 'docker-compose_script_compare.yml' if compare else 'docker-compose_script.yml'

# enables ability to add parameters for db options, version 1.28.0 or later of docker-compose is required for --profile
db = False
profile = "--profile dbs up" if db else "up"

process_cmd = f"docker-compose --file ./{docker_compose_file} --verbose {profile} -d"
process = subprocess.Popen(process_cmd, shell=True, env=myenv)

process.wait()