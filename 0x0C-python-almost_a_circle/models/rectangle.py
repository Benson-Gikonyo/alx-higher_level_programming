#!/usr/bin/python3
""" defines Rectangle class"""
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initiate Rectagle class
        """
        self.__width = width
        self._height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        @property :get width
        @width.setter: set width
        """
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """
        @property :get height
        @width.setter: set height
        """
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        """
        @property :get x
        @width.setter: set x
        """
        return self.__x

    @x.setter
    def width(self, x):
        self.__x = x

    @property
    def y(self):
        """
        @property :get width
        @width.setter: set width
        """
        return self.__y

    @width.setter
    def width(self, y):
        self.__y = y
