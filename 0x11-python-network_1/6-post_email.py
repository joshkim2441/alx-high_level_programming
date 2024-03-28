#!/usr/bin/python3
""" Takes in a URL and an email address, sends a POST to the
passed URL with the email as a parameter, and finally
displays the body of the response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    resp = requests.post(url, data=data)
    print(resp.text)
