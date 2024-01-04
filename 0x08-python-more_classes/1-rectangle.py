#!/usr/bin/python3
"""Defining a class rectangle."""


class Rectangle:
    """
    Rectangle class defines a rectangle by its width and height.
    """
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.
        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.
        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the input is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.
        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.
        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the input is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
