#!/usr/bin/python3
""" defines the add_item function"""


import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item():
    """all arguments to a Python list, and then save them to a file

    Return: add_item.json 
    """

    try:
        lst = load_from_json_file("add_item.json")
    except FileNotFoundError:
        lst = []

    lst. extend(sys.argv[1:])
    save_to_json_file(lst, "add_item.json")
