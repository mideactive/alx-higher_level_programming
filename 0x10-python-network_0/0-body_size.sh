#!/bin/bash
# A script that takes, send and display url size

url=$1

# Send a GET request to the URL and store the response body in a variable
response_body=$(curl -sL "$url")

# Calculate the size of the response body in bytes
content_length=$(echo -n "$response_body" | wc -c)

# Display the size of the response body in bytes
echo "$content_length"
