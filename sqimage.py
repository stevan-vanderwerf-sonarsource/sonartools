import subprocess
import os
import sys

# from https://github.com/axil/docker-registry-list
tags = {
    "ee950":"9.5.0-enterprise",
    "ee890":"8.9.0-enterprise"
}

# e.g. ee950
version = sys.argv[1]
# e.g. 9.5.0-enterprise
tag = tags.get(version)
# e.g. 950
tag_num = version[len(version)-3:]

# set database type, defaults to h2 if not set
db_type = 'h2' if len(sys.argv) < 3 else sys.argv[2]

myenv = {
    **os.environ,
    "BUILD": str(tag_num),
    "SQ_VERSION": str(tag),
    "DB": str(db_type)
}

# enables the ability to spin up another instance of a different version to compare
compare = False
docker_compose_file = 'docker-compose_script_compare.yml' if compare else 'docker-compose_script.yml'

# enables ability to add parameters for db options, version 1.28.0 or later of docker-compose is required
db = True
profile = "--profile dbs up" if db else "up"

process_cmd = f"docker-compose --file /home/stevanvanderwerf/code/tools/{docker_compose_file} --verbose {profile} -d"
process = subprocess.Popen(process_cmd, shell=True, env=myenv)

process.wait()
print("Completed!")