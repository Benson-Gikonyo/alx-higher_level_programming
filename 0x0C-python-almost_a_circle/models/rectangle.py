#!/usr/bin/python3
""" defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle. Inherits from base.

    Args:
        Base (class): parent class
        width (int): width of rectangle
        height (int): height of rectangle
        x (int): x coordinate
        y (int): y coordinate
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
        if self.__y:
            for i in range(self.__y):
                print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        """ return a string representation of rectangle

        Returns:
            string
        """
        string = f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return (f"[Rectangle] ({self.id}) " + string)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:

        Args:
            *args: non keyword command line arguments
        """
        attr_list = ["id", "__width", "__height", '__x', '__y']
        if args and len(args) != 0:
            for num in range(len(args)):
                if num == 0:
                    self.id = args[num]
                if num == 1:
                    self.width = args[num]
                if num == 2:
                    self.height = args[num]
                if num == 3:
                    self.x = args[num]
                if num == 4:
                    self.y = args[num]
        else:
            for kw in kwargs:
                if kw == "id":
                    self.id = kwargs[kw]
                if kw == "width":
                    self.width = kwargs[kw]
                if kw == "height":
                    self.height = kwargs[kw]
                if kw == 'x':
                    self.x = kwargs[kw]
                if kw == 'y':
                    self.y = kwargs[kw]
