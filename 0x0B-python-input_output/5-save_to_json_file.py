#!/usr/bin/python3
""" defines the save_to_json_file() function"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation:

    Args:
        my_obj (object): _description_
        filename : file to save the thing in
    """

    j_string = json.dumps(my_obj)

    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(j_string))
        f.close()
