#!/usr/bin/python3
""" Defines Base Geometry class"""


class BaseGeometry:
    """BaseGeometry class
    """
    def area(self):
        """right now, it raises an exception

        Raises:
            Exception: area not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """confirm value is an int and value > 0

        Args:
            name (str)): variable name of value
            value (int): actual value

        Raises:
            TypeError: name must be int
            ValueError: name must be > 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 1:
            raise ValueError(f"{name} must be greater than 0")
