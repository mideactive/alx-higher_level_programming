#!/usr/bin/python3
"""Get github commits for the last 10 users"""
import requests
import sys



if __name__ == "__main__":
    repository = sys.argv[1]  # Repository name
    owner = sys.argv[2]  # Owner name

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    # Send GET request to retrieve the commits
    response = requests.get(url)

    # Check the response status code
    if response.status_code == 200:
        commits = response.json()

    # Iterate over the 10 most recent commits
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
    else:
        print(response.status_code)
