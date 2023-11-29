#!/usr/bin/python3
import sys


if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)
    if num_args == 0:
        print("Number of argument: 0.")
    elif num_args == 1:
        print("Number of argument: 1:")
    else:
        print("{:d} arguments:".format(num_args))
    for i, arg in enumerate(args):
        print("{i:d}: {}".format(i+1, arg))
