#!/usr/bin/python3
"""
Defines a function that prints a square with the character #.

`size` is the size length of the square.
"""


def print_square(size):
    """
    Prints a square with the character #.
    """

    # Validate size input
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")

    # Print the square
    for i in range(size):
        print("#" * size)
