#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response for a 200 status code
curl -s "$1" -X GET -D - | awk '/HTTP\/1.1 200 OK/ {flag=1; next} flag; {if (flag) print}'
