#!/usr/bin/python3
""" defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle. Inherits from base.

    Args:
        Base (class): parent class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initiate Rectangle class
        """
        self.validate_wh(width, "width")
        self.__width = width

        self.validate_wh(height, "height")
        self.__height = height

        self.validate_xy(x, "x")
        self.__x = x

        self.validate_xy(y, "y")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        self.validate_wh(value, "width")
        self.__width = value

    @property
    def height(self):
        """
        @property :get height
        @width.setter: set height
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_wh(value, "height")
        self.__height = value

    @property
    def x(self):
        """
        @property :get x
        @width.setter: set x
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_xy(value, "x")
        self.__x = value

    @property
    def y(self):
        """
        @property :get width
        @width.setter: set width
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_xy(value, "y")
        self.__y = value

    def validate_wh(self, value, name):
        """validate width or height of rectangle

        Args:
            value (int): width or height of rectangle
            name (str): name of attribute

        Raises:
            TypeError: must be int
            ValueError: must be > 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 1:
            raise ValueError(f"{name} must be > 0")

    def validate_xy(self, value, name):
        """validate x or y attributes

        Args:
            value (int): x or y value
            name (str): name of attribute

        Raises:
            TypeError: must be an interger
            ValueError: must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """returns area of rectangle

        Return: area
        """
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #
        """
        for num in range(self.__width):
            for num2 in range(self.__height):
                print("#", end="")
            print()
        print()

    def __str__(self):
        return (f"[Rectangle] ({self.id}){self.__x}/{self.__y} - {self.__width}/{self.__height}")
