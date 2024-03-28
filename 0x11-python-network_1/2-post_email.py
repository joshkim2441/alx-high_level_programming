#!/usr/bin/python3
""" Takes in a URL and email, sends a POST request to the URL
with email as parameter, and displays the body of the
response decoded in utf-8
"""

from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = argv[1]
    val = {"emil": argv[2]}
    data = urlencode(val).encode("ascii")

    request = Request(url, data)
    with urlopen(request) as response:
        html = response.read().decode("utf-8", "replace")
        print(html)
