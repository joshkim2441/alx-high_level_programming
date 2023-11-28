#!/usr/bin/python3
def uppercase(str):
    for k in range(len(str)):
        char = ord(str[k])
        if 97 <= char <= 122:
            char = char - 32
        print("{:c}".format(char), end="")
    print()
