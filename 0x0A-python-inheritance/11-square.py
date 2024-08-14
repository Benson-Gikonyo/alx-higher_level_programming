#!/usr/bin/python3
"""defines Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle Class

    Args:
        Rectangle (class): Base class
    """
    def __init__(self, size):
        """initialize square

        Args:
            size (int): size of rectangle
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return(f"[Square] {self.__size}/{self.__size}")
