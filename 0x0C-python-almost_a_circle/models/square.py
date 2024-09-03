#!/usr/bin/python3
""" defines Class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square, a sub class  of Rectangle

    Args:
        Rectangle (class): Parent class
        size (int): length of Square
        x(int): x coordinate
        y (int): y coordinate
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets size
        Returns:
            size: size of rectangle
        """
        return self.width

    @size.setter
    def size(self, value):
        super().validate_wh(value, "width")
        self.width = value
        self.height = value

    def __str__(self):
        """ return a string representation of square

        Returns:
            string
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
