#!/usr/bin/python3
for k in range(122, 96, -1):
    char = k
    if k % 2 != 0:
        char = char - 32
    print("{:c}".format(char), end="")
