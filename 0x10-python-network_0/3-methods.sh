#!/bin/bash
# A script that takes a url and displays all HTTP methods
curl -sI "$1" | grep -i "Allow" | cut -d " " -f2-
