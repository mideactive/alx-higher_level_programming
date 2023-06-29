#!/usr/bin/env bash
# A script that takes, send and display url size

# Send a request to the URL and store the response body in a variable
url=$1

# Send a HEAD request to the URL and store the response header in a variable
response_header=$(curl -sI "$url")

# Extract the Content-Length field from the response header
content_length=$(echo "$response_header" | awk '/Content-Length/ {print $2}' | tr -d '\r')

# Display the size of the response body in bytes
echo "$content_length"

