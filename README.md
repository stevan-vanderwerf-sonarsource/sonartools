# tools
Tools for testing multiple versions of SonarQube

# Setup
The `sqfunctions.sh` file can be initialized into your .bashrc profile (or .zsh etc) through the 'source' command
e.g. 

    if [ -f ~/code/tools/sqfunction.sh ]; then
        echo -n "sourcing ../tools/sqfunction.sh"
        source ~/code/tools/sqfunction.sh && echo "...done" || echo "...FAIL"
    fi

Make sure to initialize the `$scriptpath` and  `$ngrokprofile` variable somewhere (can be in .bashrc, etc)
e.g.

    export scriptpath='~/code/tools'
    export ngrokprofile='~/sq'
    
# Commands
Spin up a SonarQube Docker instance:

    squp $ee93
    
Spin down current SonarQube Docker instance:

    sqdn
    
Open a bash terminal on the running SonarQube Docker instance:

    dkssh
    
Get all available Docker tags for SonarQube filtered by type:

    dktags enterprise
