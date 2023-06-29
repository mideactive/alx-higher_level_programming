#!/usr/bin/env bash
# A script that takes a URL
# Sends request to the URL
# Displays the size of the body
# The curl command must be used

# Send a request to the URL and store the response body in a variable
echo $(curl -s -w %{size_download} -o /dev/null "$url")

