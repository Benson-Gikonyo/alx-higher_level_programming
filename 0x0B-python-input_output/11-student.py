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
        if type(attrs) is list:
            new_dict = {}
            for key in self.__dict__:
                for key2 in attrs:
                    if key == key2:
                        new_dict[key] = self.__dict__[key]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            if key == "first_name":
                self.first_name = json[key]
            if key == "last_name":
                self.last_name = json[key]
            if key == "age":
                self.age = json[key]
