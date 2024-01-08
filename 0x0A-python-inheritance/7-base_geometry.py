#!/usr/bin/python3
""""Defines a class representing a base geometry."""


class BaseGeometry:
    """
    A base class representing a generic geometry.
    """
    def area(self):
        """
        Raises an exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value, raising TypeError or ValueError exceptions
        if needed.

        Args:
            name (str): The name of the variable being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
