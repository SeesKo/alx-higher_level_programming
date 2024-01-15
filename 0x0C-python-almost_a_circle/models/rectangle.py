#!/usr/bin/python3
"""
Module defining a `Rectangle` class.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle.
            y (int): Y-coordinate of the rectangle.
            id (int): If provided, assign to the public instance attribute id.
                    Else, use the logic of the __init__ of the Base class.
        """
        if id is not None:
            if not isinstance(id, int):
                raise TypeError("id must be an integer")
            elif id < 0:
                raise ValueError("id must be >= 0")

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): Value to set for the width attribute.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): Value to set for the height attribute.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Args:
            value (int): Value to set for the x attribute.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Args:
            value (int): Value to set for the y attribute.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Calculate and return the area of the Rectangle instance.

        Returns:
            int: Area value.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance with the character # to stdout,
        taking into account the x and y coordinates.
        """
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.

        Returns:
            str: String representation of the Rectangle instance.
        """
        return (
                f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}"
                )

    def to_dictionary(self):
        """
        Return the dictionary representation of the Rectangle instance.

        Returns:
            dict: Dictionary representation of the Rectangle instance.
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """
        Update the Rectangle instance attributes with the provided arguments.

        Args:
            args (tuple): Tuple of arguments in the order:
                            id, width, height, x, y.
            kwargs (dict): Dictionary of key-value pairs representing
                            attributes.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
