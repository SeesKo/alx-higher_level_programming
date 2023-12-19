#!/usr/bin/python3
"""Defining a class square"""


class Square:
    """A class representing a square"""

    def __init__(self, size=0):
        """Initialize a new instance of the Square class.

        Args:
            size (float or int, optional): The size of the square.
            Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for retrieving the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for setting the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison based on square area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Inequality comparison based on square area."""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Greater than comparison based on square area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Greater than or equal to comparison based on square area."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """Less than comparison based on square area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Less than or equal to comparison based on square area."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
