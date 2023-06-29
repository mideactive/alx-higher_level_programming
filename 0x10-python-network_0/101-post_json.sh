#!/bin/bash
# Display JSON POST sent to a URL
curl -s -X POST -H "Content-Type: application/json" -d $(cat "$2") "$1"
