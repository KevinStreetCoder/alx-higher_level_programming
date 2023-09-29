#!/usr/bin/python3
"""
Fetches and lists 10 most recent commits of a repository.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: ./100-github_commits.py <repository name> <owner name>")
    
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    
    try:
        response = requests.get(url)
        commits = response.json()
        
        for commit in commits[:10]:  # Limit to the 10 most recent commits
            sha = commit.get("sha")
            author = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author}")
    except requests.exceptions.RequestException as e:
        sys.exit(f"Error: {e}")

