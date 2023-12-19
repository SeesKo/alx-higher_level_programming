#!/usr/bin/python3
"""Defining a class square"""


class Square:
    """A class representing a square"""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
