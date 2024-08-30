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
