#!/usr/bin/python3
""" defines the to_json_string function """


def to_json_string(my_obj):
    import json

    """ returns the JSON representation of an object (string)

    Args:
    my_obj(obj): object

    Return: string
    """
    return json.dumps(my_obj)
