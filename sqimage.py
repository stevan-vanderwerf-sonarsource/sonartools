import subprocess

subprocess.call([
    'docker-compose', '--file', './docker-compose1.yml', 'up', '-d',
    ])