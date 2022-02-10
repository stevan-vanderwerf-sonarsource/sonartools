# to initialize this into your .bashrc profile (or .zsh etc) add an export to this file
# make sure to initialize the "$scriptpath" variable somewhere (can be in .bashrc, etc)
# make sure to initialize the "$ngrokprofile" variable somewhere (can be in .bashrc, etc)
# e.g. 
# if [ -f /home/stevanvanderwerf/code/tools/sqfunction.sh ]; then
#     echo -n "sourcing ../tools/sqfunction.sh"
#     source /home/stevanvanderwerf/code/tools/sqfunction.sh && echo "...done" || echo "...FAIL"
# fi
# export scriptpath='/home/stevanvanderwerf/code/tools'
# export ngrokprofile='sq'


# ngrok status
alias ngst='jobs'

alias ngdn="kill %$(jobs | grep ngrok | grep -Po '(?<=\[)\d+(?=\])')"
alias ngup="ngrok start "$ngrokprofile" > /dev/null &"

# command to spin up a SonarQube Docker container and ngrok instance
# needs 1 command line argument of the SonarQube version:
# e.g. squp $ee89
squp() {
    ngrok start "$ngrokprofile" > /dev/null &
    # sanity check to make sure that ngrok start succeeded
    ngst
    export SQ_VERSION="$1"
    docker-compose -f "$scriptpath"/docker-compose.yml up -d
    docker ps
}

# command to spin down the current SonarQube Docker container and ngrok instance
sqdn() {
    docker-compose -f "$scriptpath"/docker-compose.yml down
    ngdn
    ngst
    # sanity check to make sure that no docker sq docker containers are still running
    docker ps
}

# Docker command that opens a bash terminal in the currently running SonarQube docker container
# in this script all SonarQube docker containers are names 'sqb'
dockerexec() {
    docker exec -it "$1" /bin/bash
}
alias dkssh="dockerexec sqb"


# gets all the available Docker tags, you can narrow down the list by specifying the version:
# e.g. dktags enterprise

dktags() {
    wget -q https://registry.hub.docker.com/v1/repositories/sonarqube/tags -O - |
    sed -e 's/[][]//g' -e 's/"//g' -e 's/ //g' |
    tr '\}' '\n' |
    awk -F: '{print $3}' | grep "$1"
}

# specifying these variables manually means you do not have to write out the full Docker tag in the command: 
# e.g. squp $ee89

# only the community version of 7.9 is officially dockerized
export ee79='7.9-community'

export ee82='8.2-enterprise'
export ee83='8.3-enterprise'
export ee831='8.3.1-enterprise'
export ee84='8.4-enterprise'
export ee840='8.4.0-enterprise'
export ee841='8.4.1-enterprise'
export ee842='8.4.2-enterprise'
export ee85='8.5-enterprise'
export ee850='8.5.0-enterprise'
export ee851='8.5.1-enterprise'
export ee86='8.6-enterprise'
export ee860='8.6.0-enterprise'
export ee861='8.6.1-enterprise'
export ee87='8.7-enterprise'
export ee870='8.7.0-enterprise'
export ee871='8.7.1-enterprise'
export ee88='8.8-enterprise'
export ee880='8.8.0-enterprise'
export ee89='8.9-enterprise'
export ee890='8.9.0-enterprise'
export ee891='8.9.1-enterprise'
export ee892='8.9.2-enterprise'
export ee893='8.9.3-enterprise'
export ee894='8.9.4-enterprise'
export ee895='8.9.5-enterprise'
export ee896='8.9.6-enterprise'
export ee9='9-enterprise'
export ee90='9.0-enterprise'
export ee900='9.0.0-enterprise'
export ee901='9.0.1-enterprise'
export ee91='9.1-enterprise'
export ee910='9.1.0-enterprise'
export ee92='9.2-enterprise'
export ee920='9.2.0-enterprise'
export ee921='9.2.1-enterprise'
export ee922='9.2.2-enterprise'
export ee923='9.2.3-enterprise'
export ee924='9.2.4-enterprise'
export ee93='9.3-enterprise'
export ee930='9.3.0-enterprise'