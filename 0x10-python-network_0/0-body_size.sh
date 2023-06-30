#!/bin/bash
# A script that takes, send and display url size
echo $(curl -s --head "$1"  | grep -i Content-Length | awk '{print $2}')
