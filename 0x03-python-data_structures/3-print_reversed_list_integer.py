#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints list's integers in reverse order"""

    # Checking if list is not empty
    if (my_list):
        my_list.reverse()

        for i in (my_list):
            print("{:d}".format(i))
