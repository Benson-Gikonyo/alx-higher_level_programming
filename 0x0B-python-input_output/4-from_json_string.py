#!/usr/bin/python3
""" defines the from_json_string(my_str) function"""


import json


def from_json_string(my_str):
    """returns a Python object represented by a JSON string:

    Args:
        my_str (string): Json string representation of python
        object

    Return: python object
    """
    return json.loads(my_str)
