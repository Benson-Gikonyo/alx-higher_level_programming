#!/usr/bin/python3
"""  Defines Base class"""


import json


class Base:
    """Base class
    Args:
        id (int): Identifier
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries=None):
        """that returns the JSON string representation
        of list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries

        Return: string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
