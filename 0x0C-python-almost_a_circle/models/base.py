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

    @classmethod
    def save_to_file(cls, list_objs=None):
        """writes the JSON string representation of
        list_objs to a file

        Args:
            list_objs (list):  list of instances who inherits
            of Base
            cls: file name
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        string = Base.to_json_string(list_dicts)

        with open(filename, "w") as f:
            f.write(string)
            f.close()

    @staticmethod
    def from_json_string(json_string=None):
        """returns the list of the JSON string representation 'json_string'

        Args:
            json_string (str): JSON string representation

        Return: list
        """
        if json_string is None or len(json_string) == 0:
            return []

        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1, 0, 0)
        elif cls.__name__ == "Square":
            instance = cls(1, 0, 0)
        else:
            instance = cls()
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances

        Args:
            cls: file
        """
        instances = []

        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                list_repr = cls.from_json_string(f.read())
                instances = [cls.create(**repr) for repr in list_repr]
                f.close()
        except FileNotFoundError:
            pass

        return instances
