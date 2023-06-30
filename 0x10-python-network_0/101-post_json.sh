#!/bin/bash
# Display JSON POST sent to a URL
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
