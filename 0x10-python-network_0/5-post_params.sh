#!/bin/bash
# This script sends a POST request to a URL with specified parameters and displays the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
