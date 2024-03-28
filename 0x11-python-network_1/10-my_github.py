#!/usr/bin/python3
""" Takes GitHub credentials and uses the GitHub PI to ddisplay id """
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    auth = HTTPBasicAuth(username, token)

    response = requests.get('https://api.github.com/user',
                            auth=auth)
    print(response.json().get('id'))
