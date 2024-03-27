#!/bin/bash
# Send GET request to the URL with X-School-User-Id header set to 98 and display the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
