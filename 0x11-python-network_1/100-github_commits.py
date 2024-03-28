#!/usr/bin/python3
""" Takes 2 arguments to list 10 commits, recent to oldest,of
the repository 'rails' by the user 'rails'
"""
import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}'.format(owner_name,
                                                      repo_name) + '/commits'
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        print("{}:{}".format(commit.get('sha'), commit.get(
             'commit').get('author').get('name')))
