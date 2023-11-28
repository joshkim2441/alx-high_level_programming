#!/usr/bin/python3
"""print the lowercase alphabet without a newline"""

for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
