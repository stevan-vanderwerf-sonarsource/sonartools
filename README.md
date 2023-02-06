# sonarqube tools
Tools for testing multiple versions of SonarQube using Docker images

# Pre-requisites
The pre-requisites for running this script are having docker and docker-compose installed. 
Additionally, docker-compose needs to be >= v1.28.0 to take advantage of the --profile parameter

# Running script
The script is run by calling the sonar.py entrypoint, for example:
`python3 sonar.py -up ee980`

# Tips
To make things easier you can add the following lines to your `~/.bashrc` file:

    alias sonarup='[path-to-project]/sonar.py -up'
    alias sonardn='[path-to-project]/sonar.py -dn'
    alias sonar='[path-to-project]/sonar.py'
    
# Usage examples
spins up the v9.8.0 version of SonarQube Docker image:

    sonarup ee980
    
spins down the running Docker image:

    sonardn
    
prints the command parameter options and their description:    

    sonar -h
