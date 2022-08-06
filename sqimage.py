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

process = subprocess.Popen(['docker-compose', '--file', "/home/stevanvanderwerf/code/tools/docker-compose.yml.bak2", '--verbose', 'up', '-d'], env=myenv)
process.wait()
print("Completed!")