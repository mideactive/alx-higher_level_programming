#!/bin/bash
# A script that sends a message and gets a response from the server
curl -s -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
