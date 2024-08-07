#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle.
"""


class Rectangle():
    """class that defines a rectangle based on 0-rectangle.py

        Attributes:
            width (int): width of rectangle
            height (int): height of rectangle
    """
    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        """initialise the Rectangle class
        Args:
            width (int, optional): width of rectangle.
            height (int, optional): height of rectangle .
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        @property -gets width of rectangle
        @width.setter - validates and sets width

        Returns:
            width(int)
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        @property -gets height of rectangle
        @width.setter - validates and sets height

        Returns:
            height(int)
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
