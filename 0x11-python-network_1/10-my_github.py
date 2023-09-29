#!/usr/bin/python3
"""
Takes GitHub credentials (username and password) and uses the GitHub API to display the user's id using Basic Authentication with a personal access token as the password.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    
    response = requests.get('https://api.github.com/user', auth=(username, password))
    
    try:
        data = response.json()
        print(data.get("id"))
    except ValueError:
        print(None)

