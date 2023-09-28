#!/bin/bash
# This script sends a GET request to a URL with a custom header and displays the body of the response
curl -s "$1" -X GET -H "X-School-User-Id: 98"
