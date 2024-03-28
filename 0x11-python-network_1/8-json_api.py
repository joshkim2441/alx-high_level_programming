#!/usr/bin/python3
""" Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as parameter
"""

import sys
import json
import requests

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    rsp = requests.post(url, data={'q': q})
    try:
        rsp_dict = rsp.json()
        id, name = rsp_dict.get('id'), rsp_dict.get('name')
        if len(rsp_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(rsp_dict.get(
                'id'), rsp_dict.get('name')))
    except Exception:
        print("Not a valid JSON")
