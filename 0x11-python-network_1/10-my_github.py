#!/usr/bin/python3
""" Takes GitHub credentials and uses the GitHub PI to ddisplay id """
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get('https://api.github.com/user',
                            auth=(username, token))

    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("Error: {}".format(response.status_code))
