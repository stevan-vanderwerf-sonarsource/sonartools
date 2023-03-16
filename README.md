# sonar tools
Tools for testing multiple versions of SonarQube using Docker images

# Pre-requisites
The pre-requisites for running this script are having docker and docker-compose installed. 
Additionally, docker-compose needs to be >= v1.28.0 to take advantage of the --profile parameter

# Running script
The script is run by calling the sonar.py entrypoint, for example:
`python3 sonar.py -up ee980`

Any tag/version of SonarQube available in Dockerhub can be used including (except Datacenter edition), but each tag much be 3 digits, e.g.
* Community Edition: ce791 (oldest available tag)
* Developer Edition: de899

# Tips
To make things easier you can add the following lines to your `~/.bashrc` file:

    alias sonarup='[path-to-project]/sonar.py -up'
    alias sonardn='[path-to-project]/sonar.py -dn'
    alias sonar='[path-to-project]/sonar.py'
    
# Usage examples
spins up the v9.9.0 version of SonarQube Docker image:

    sonarup ee990
    
spins down the running Docker image:

    sonardn
    
prints the command parameter options and their description:    

    sonar -h

# Advanced examples
run SonarQube with an external database (currently only Postgres supported in this tool - defaults to Postgres 13)

    sonarup ee990 -db pg
    
run SonarQube with a specific version of an external database

    sonarup ee990 -db pg -dbv 15
    
# Docker Desktop configuration
This script can work as a command line tool only, or it can be run in conjunction with Docker Desktop. Check your `docker context` to see if your Docker configuration is command line only or if it is set to run Docker powering the Docker Desktop (in which case the Containers/Images/Volumes will be displayed in Docker Desktop UI)

    # list the available Docker 'contexts'
    $>  docker context ls
    $>  NAME                TYPE                DESCRIPTION                               DOCKER ENDPOINT
        default       *     moby                Current DOCKER_HOST based configuration   unix:///var/run/docker.sock          
        desktop-linux       moby                                                          unix:///home/user/.docker/desktop/docker.sock

If the context of your terminal is showing to be 'default' then run the following command to change the context to Docker Desktop

    $> docker context use $(docker context ls | grep desktop | cut -d ' ' -f 1)
    
# Volumes
By default when each SonarQube version is spun up it will create 4 volumes:
* db        - persists the contents of the database
* esdata    - persists the the data folder
* logs      - persists the logs folder
* plugins   - persists the plugins folder
