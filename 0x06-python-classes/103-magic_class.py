#!/usr/bin/python3

"""Defines a class magical circle"""

import math


class MagicClass:
    """Class representing magical circle with radius-based calculations"""

    def __init__(self, radius=0):
        """Initialize an instance of the MagicClass.

        Args:
            radius (float or int, optional): The radius of the circle.
            Defaults to 0.

        Raises:
            TypeError: If radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
