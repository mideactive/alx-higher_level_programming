#!/bin/bash
# A script that takes, sends, and displays POST request passed to a URL
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
