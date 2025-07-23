#!/usr/bin/python3
""" Lists 10 most recent commits from a GitHub repo using GitHub API """

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
    except Exception as e:
        pass

