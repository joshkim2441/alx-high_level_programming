#!/usr/bin/python3
""" Takes in a URL, sends a request to it and displays
the body of the rsponse decoded in utf-8
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
