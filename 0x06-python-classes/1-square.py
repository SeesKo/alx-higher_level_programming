#!/usr/bin/python3
"""Defining a class square"""


class Square:
    """A class representing a square"""

    def __init__(self, size):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square. Must be an integer.

        Raises:
            TypeError: If the size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
