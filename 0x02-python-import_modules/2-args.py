#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # Subtracting 1 coz the 1st element in
    # argv is the script name itself.
    num_args = len(argv) - 1

    if num_args == 0:
        print("0 arguments", end="")
        print(".")
    else:
        print("{} argument{}:".format(num_args, "s" if num_args > 1 else ""))
        # 'enumerate' is used to get both the index (i)
        # and the value of each argument (arg)
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
