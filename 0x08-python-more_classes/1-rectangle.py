#!/usr/bin/python3
"""Defining a class rectangle."""


class Rectangle:
    """
    Rectangle class defines a rectangle by its width and height.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes width and height
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
