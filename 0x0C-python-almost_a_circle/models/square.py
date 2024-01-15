#!/usr/bin/python3
"""
Module defining a `Square` class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square.
            y (int): Y-coordinate of the square.
            id (int): If provided, assign to the public instance attribute id.
                    Else, use the logic of the __init__ of the Rectangle class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): Value to set for the size attribute.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square instance attributes with the provided arguments.

        Args:
            args (tuple): Tuple of arguments in the order: id, size, x, y.
            kwargs (dict): Dictionary of key-value pairs representing
                            attributes.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square instance.

        Returns:
            dict: Dictionary representation of the Square instance.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: String representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
