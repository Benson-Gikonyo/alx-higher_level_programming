#!/usr/bin/python3
"""defines MyInt class"""


class MyInt(int):
    """ interger class with inverted operators
    """

    def __init__(self, number):
        self.__number = number

    def __eq__(self, num):
        return super().__ne__(num)

    def __ne__(self, num):
        return super().__eq__(num)

    def __str__(self):
        return f"{self.__number}"
