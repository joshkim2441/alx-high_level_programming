#!/bin/bash
# Takes in a URL, sends a request to it and displays the response body
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
