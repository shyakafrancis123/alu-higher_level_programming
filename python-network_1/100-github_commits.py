#!/usr/bin/python3
"""
This script uses the GitHub API to list the 10 most recent commits
of a given repository by a specified owner.

Usage:
    ./100-github_commits.py <repository name> <owner name>

Example:
    ./100-github_commits.py rails rails

Output format:
    <sha>: <author name>
"""

import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        response = requests.get(url)
        commits = response.json()

        for commit in commits[:10]:
            sha = commit.get("sha")
            author = commit.get("commit", {}).get("author", {}).get("name")
            print(f"{sha}: {author}")
    except Exception:
        pass

