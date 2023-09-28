#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a JSON file and displays the response
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON File>"
    exit 1
fi

URL="$1"
JSON_FILE="$2"

# Check if the JSON file is valid
if ! jq . "$JSON_FILE" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

curl -s -X POST -H "Content-Type: application/json" -d @"$JSON_FILE" "$URL"
