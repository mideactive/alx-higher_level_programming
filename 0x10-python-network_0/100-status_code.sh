#!/bin/bash
# A scriptthat sends URL request as argument and displays only status code
curl -sLw "%http_code" -o /dev/null "$1"
