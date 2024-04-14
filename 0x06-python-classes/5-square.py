#!/usr/bin/python3
"""
A class Square that defines a square of size 'size',
like in 4-square.py.

"""


class Square():
    """
    defines a square

    Attributes:
        size (int): size of square
    """
    __size = None

    def __init__(self, size=0):
        """initialize Square

        Args:
            size (int):  length of square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        @property: returns/gets  size of Square
        @size.setter: validates and sets the size of Square
        """
        return self.__size

    @size.setter
    def size(self, value=0):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """calculates area of square

        Returns:
            int:  area of square
        """
        return self.__size ** 2

    def my_print(self):
        """prints the square in stdout using '#'
        return : nothing
        """
        if self.size == 0:
            print()

        for num in range(self.size):
            for num2 in range(self.size):
                print("#", end="")
            print()
