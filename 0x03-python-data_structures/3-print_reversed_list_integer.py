#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints list's integers in reverse order"""

    my_list.reverse()

    for i in (my_list):
        print("{:d}".format(i))
