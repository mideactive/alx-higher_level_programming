#!/usr/bin/env bash
# A script that takes a URL
# Sends request to the URL
# Displays the size of the body
# The curl command must be used
if [ $# -eq 0 ]; then
	echo "Please provide URL."

	exit 1
fi

url=$1
response=$(curl -sSL -w "%{size_download}" -o /dev/null "$url")
echo "$response"
