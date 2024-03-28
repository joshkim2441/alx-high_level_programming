#!/usr/bin/python3
""" Takes in a URL, sends a request to it and displays
the value of the variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    resp = requests.get(url)

    print(resp.headers.get('X-Request-Id'))
