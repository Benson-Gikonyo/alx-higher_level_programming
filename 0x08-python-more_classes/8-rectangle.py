#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle.
"""


class Rectangle():
    """class that defines a rectangle based on 5-rectangle.py

        Attributes:
            width (int): width of rectangle
            height (int): height of rectangle
            number_of_instances (int): number of instances of rectangle
    """
    __width = None
    __height = None
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialise the Rectangle class
            Also increase the number of instances counter
        Args:
            width (int, optional): width of rectangle.
            height (int, optional): height of rectangle .
        """
        Rectangle.number_of_instances += 1
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

    def area(self):
        """calculate area of rectangle

        Returns:
            area (int): area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """calculate perimeter of rectangle

        Returns:
            perimeter(int): perimeter of rectangles
        """
        perimeter = 0
        if self.__width == 0 or self.__height == 0:
            return perimeter
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """returns a string of the rectangle
        with the '#' character
        """
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect

        for num in range(0, self.__height):
            for num2 in range(0, self.__width):
                rect += str(self.print_symbol)
            if num == self.__height - 1:
                continue
            else:
                rect += "\n"

        return rect

    def __repr__(self):
        """ return a string representation of the rectangle
        """
        rect_str = "Rectangle(" + str(self.__width) + ", " + \
            str(self.__height) + ")"

        return rect_str

    def __del__(self):
        """prints a string and deletes an object
            Decrease the number of instances counter
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        del self

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.area()
        area2 = rect_2.area()
        bigger = None
        if area1 == area2:
            return rect_1
        else:
            bigger = max(area2, area1)

        return bigger
