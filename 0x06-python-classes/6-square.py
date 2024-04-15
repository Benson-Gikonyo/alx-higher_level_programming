#!/usr/bin/python3
"""
A class Square that defines a square of size 'size',
like in 5-square.py.

"""


class Square():
    """
    defines a square

    Attributes:
        size (int): size of square
        position (tuple): position of the square.
    """
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        """initialize Square

        Args:
            size (int):  length of square. Defaults to 0.
            position (tuple): position of the square.Defaults to (0,0)
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        @property: return/get position
        position.setter: validate and assign/set the position values

        """
        return self.__position

    @position.setter
    def position(self, value):
        # check type of value
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        # check for nested tuples
        if any(type(value[idx]) is tuple for idx in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        # check for number of elements
        # or (len(value[idx]) for idx in value)
        if (len(value) > 2):
            raise TypeError("position must be a tuple of 2 positive integers")

        # check for type of elements
        if (type(value[0]) is not int) or (type(value[1]) is not int):

            raise TypeError("position must be a tuple of 2 positive integers")

        # check if values are +ve intergers
        if (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.position = tuple(value)

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
            for num in self.position:
                print(num * " ", end="")
            for num2 in range(self.size):
                print("#", end="")
            print()
