#!/usr/bin/python3
""" Takes in a URL, sends a request to it and
displays the value of the 'X-Request-Id' variable
found in the header of the reponse """

import sys
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = sys.argv[1]
    res = Request(url)

    with urlopen(res) as response:
        print(dict(response.headers).get('X-Request-Id'))
