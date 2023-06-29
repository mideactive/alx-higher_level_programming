#!/usr/bin/env bash
# A script that takes a URL
# Sends request to the URL
# Displays the size of the body
# The curl command must be used
#!/bin/bash

# Send a request to the URL and store the response body in a variable
curl -sI "$1" | grep "Content-Length" | awk '{print $2}'

