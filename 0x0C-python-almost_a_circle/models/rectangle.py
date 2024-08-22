#!/usr/bin/python3
""" defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle. Inherits from base.

    Args:
        Base (class): parent class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initiate Rectagle class
        """
        self.__width = self.set_width(width)
        self.__height = self.set_height(height)
        self.__x = self.set_x(x)
        self.__y = self.set_y(y)
        super().__init__(id)

    @property
    def width(self):
        """
        @property :get width
        @width.setter: set width
        """
        return self.__width

    @width.setter
    def set_width(self, width):
        self.__width = width

    @property
    def height(self):
        """
        @property :get height
        @width.setter: set height
        """
        return self.__height

    @height.setter
    def set_height(self, height):
        self.__height = height

    @property
    def x(self):
        """
        @property :get x
        @width.setter: set x
        """
        return self.__x

    @x.setter
    def set_x(self, x):
        self.__x = x

    @property
    def y(self):
        """
        @property :get width
        @width.setter: set width
        """
        return self.__y

    @y.setter
    def set_y(self, y):
        self.__y = y
