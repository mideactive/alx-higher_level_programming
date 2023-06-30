#!/bin/bash
# A scriptthat sends URL request as argument and displays only status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
