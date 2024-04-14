#!/usr/bin/python3
"""
A class Square that defines a square of size 'size'
"""


class Square():
    """
    defines a square

    Attributes:
        size: size of square
    """
    __size = None

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size ** 2
