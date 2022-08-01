import subprocess
import os

myenv = {
    **os.environ,
    "BUILD": str('899'),
    "SQ_VERSION": str('8.9.9-enterprise')
}

process = subprocess.Popen(['docker-compose', '--file', "/home/stevanvanderwerf/code/tools/docker-compose.yml.bak2", '--verbose', 'up', '-d'], env=myenv)
process.wait()
print("Completed!")