#!/bin/bash
# This shell script deploys a new version to a server.

ssh -tt
export PA_USER=Andrew1531

if [ -z "$SDE_PA_PWD" ]
then
    echo "The PythonAnywhere password var (SDE_PA_PWD) must be set in the env."
    exit 1
fi

echo "SSHing to PythonAnywhere."
sshpass -p $SDE_PA_PWD ssh -tt "StrictHostKeyChecking no" $PA_USER@ssh.pythonanywhere.com << EOF
    cd SDE-project; ./rebuild.sh
EOF
