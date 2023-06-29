#!/bin/bash
# A script that takes a url and displays all HTTP methods
curl -s  -X OPTIONS -I $1 | grep -i allow
