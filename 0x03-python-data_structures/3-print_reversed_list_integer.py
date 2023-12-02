#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints list's integers in reverse order"""

    reverse_list = reversed(my_list)

    for i in (reverse_list):
        print("{:d}".format(i))
