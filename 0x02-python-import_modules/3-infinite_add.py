#!/usr/bin/python3
import sys


def add_args():
    # Initialize the sum to 0
    sum_args = 0

    # Iterate over the arguments
    for arg in sys.argv[1:]:
        # Convert the arg to an int and add it to sum
        sum_args += int(arg)

        # Print the sum
    print(sum_args)


if __name__ == "__main__":
    add_args()
