#!/bin/bash
# Takes URL as input and displays all HTTP methods server will accept
curl -sI -X OPTIONS "$1" | grep -i Allow | cut -d " " -f 2-
