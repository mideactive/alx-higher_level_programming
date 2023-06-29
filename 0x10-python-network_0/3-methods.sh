#!/bin/bash
# A script that takes a url and displays all HTTP methods
curl -s "$1" -X OPTIONS -i | grep -i allow
