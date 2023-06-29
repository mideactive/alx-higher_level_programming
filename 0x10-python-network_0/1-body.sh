#!/bin/bash
# a script that takes, send and displays url body response
echo $(curl -sL $1 | awk 'NR==1,/HTTP\/1.1 200 OK/{p=1}p' | tail -n +5)
