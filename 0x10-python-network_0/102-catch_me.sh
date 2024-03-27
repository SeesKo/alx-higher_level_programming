#!/bin/bash
# Makes request to 0.0.0.0:5000/catch_me that causes the server to respond with a message
curl -s -X PUT 0.0.0.0:5000/catch_me -L -d "user_id=98" -H "Origin: OriginPoint"
