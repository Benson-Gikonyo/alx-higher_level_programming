#!/usr/bin/python3
""" defines the load_from_json_file() function"""


import json


def load_from_json_file(filename):
    """creates an Object from a JSON file:

    Args:
        filename : json file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
        f.close()
