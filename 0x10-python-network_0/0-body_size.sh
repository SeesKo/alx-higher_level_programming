#!/bin/bash
# Sends a request to a URL using curl and displays the body size of the response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
