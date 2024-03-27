#!/bin/bash
# Sends request to the URL and display only the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
