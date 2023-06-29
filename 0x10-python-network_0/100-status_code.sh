#!/bin/bash
# A scriptthat sends URL request as argument and displays only status code
curl -s -w "%http_code" "$1"
