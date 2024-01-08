#!/usr/bin/python3
"""Module for Square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class representing a square.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return the square description.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
