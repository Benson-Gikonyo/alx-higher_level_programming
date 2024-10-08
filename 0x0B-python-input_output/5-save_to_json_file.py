#!/usr/bin/python3
""" defines the save_to_json_file() function"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation:

    Args:
        my_obj (object): _description_
        filename : file to save the thing in
    """

    with open(filename, "w") as f:
        json.dump(my_obj, f)
        f.close()
