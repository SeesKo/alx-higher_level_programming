#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # Skip the 1st element (script name) and
    # convert each argument into an integer.
    args = [int(arg) for arg in argv[1:]]

    # Calculate the sum of all integers in arguments list
    result = sum(args)

    # Print the result
    print(result)
