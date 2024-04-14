#!/usr/bin/python3
"""
A class Square that defines a square of size 'size',
like in 3-square.py

"""


class Square():
    """
    defines a square

    Attributes:
        size: size of square
    """
    __size = None

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value=0):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2
