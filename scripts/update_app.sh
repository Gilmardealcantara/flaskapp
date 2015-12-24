#!/bin/bash
#Update and do access test
export DEPLOY_ROOT="/home/fred/dev/projects/flaskapp"
export DEPLOY_BRANCH="dev"
export DEPLOY_CURRENT_BRANCH=$(cd $DEPLOY_ROOT && git rev-parse --symbolic-full-name --abbrev-ref HEAD)

IP="$(ip addr show eth0 | grep 'inet ' | cut -f2 | awk '{ print $2}')"

echo -e "git_pull_release: Welcome to '$(hostname -f)' (${IP})\n$(date)\n"

#Check if branch is release
if [ "${DEPLOY_CURRENT_BRANCH}" != "${DEPLOY_BRANCH}" ]; then
    cd $DEPLOY_ROOT && git checkout dev
    export DEPLOY_CURRENT_BRANCH="dev"
    echo "Current branch is now '$DEPLOY_CURRENT_BRANCH'"
fi

#Pull from branch release
cd $DEPLOY_ROOT && git pull origin dev

#Execute python script to test access
#Certify last version of selenium is installed (pip install -U selenium)
#and phantomjs (https://gist.github.com/julionc/7476620 - install_phantomjs.sh)
cd $DEPLOY_ROOT && python scripts/access_test.py