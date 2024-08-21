#!/usr/bin/python3
""" defines class Student with def to_json(self) method"""


class Student:
    """Student class
    """
    def __init__(self, first_name, last_name, age):
        """initialize Student class

        Args:
            first_name (str)
            last_name (str)
            age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ that retrieves a dictionary
        representation of a Student instance 

        Returns:
            dict
        """
        return self.__dict__
