#!/usr/bin/python3
"""Defines a class that inherits a list class."""


class MyList(list):
    """
    A custom list class that inherits the built-in list class.
    """
    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        print(sorted(self))
