#!/usr/bin/python3
""" defines class Student with def to_json(self) method"""


class Student:
    """Student class
    """

    def __init__(self, first_name, last_name, age):
        self.firstname = first_name
        self.lastname = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
