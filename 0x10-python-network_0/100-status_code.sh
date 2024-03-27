#!/bin/bash
# Sends a request to a URL passed as argument, and displays only the status code of the response
curl -s -L -X HEAD -w "%{http_code}" "$1"
