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

myenv = {
    **os.environ,
    "BUILD": str(tag_num),
    "SQ_VERSION": str(tag)
}

# enables the ability to spin up another instance of a different version to compare
compare = True
docker_compose_file = 'docker-compose_script_compare.yml' if compare else 'docker-compose_script.yml'

process = subprocess.Popen([ \
    'docker-compose', \
    '--file', "/home/stevanvanderwerf/code/tools/" + docker_compose_file, \
    '--verbose', \
    'up', \
    '-d'], \
    env=myenv)

process.wait()
print("Completed!")