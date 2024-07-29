#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle.
"""


class Rectangle():
    """
    defines a rectangle based on 0-rectangle.py

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
    """
    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        """ Initialize the newly created object after
        instantiation with newly created objects

        Args:
            width (int): rectangle width. Defaults to 0.
            height (int): rectangle height. Defaults to 0.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = 0

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = 0

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
