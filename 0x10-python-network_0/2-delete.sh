#!/bin/bash
# A script that sends delete request to the URL passed passed a s the first argument
curl -s -X DELETE $1
