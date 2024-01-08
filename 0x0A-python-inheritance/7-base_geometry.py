#!/usr/bin/python3
""""Defines a class representing a base geometry."""


class BaseGeometry:
    """
    A base class representing a generic geometry.
    """
    def area(self):
        """
        Raise an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value, raising TypeError or ValueError exceptions
        if needed.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
