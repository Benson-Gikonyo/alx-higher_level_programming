#!/usr/bin/python3
""" Defines Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class based on Base Geometry class
    """
    def __init__(self, width, height):
        """initializes BaseGeometry class

        Args:
            width (int): _description_
            height (int): _description_
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """right now, it raises an exception

            Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        return self.__width * self.__height

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

    def __str__(self):
        """return rectangle description
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")