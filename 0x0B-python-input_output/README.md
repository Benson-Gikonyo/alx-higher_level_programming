Python - Input/Output 

Task 0: Write a function that reads a text file (UTF8) and prints it to stdout:

    Prototype: def read_file(filename="")

Task 1: Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

    Prototype: def write_file(filename="", text=""):

Task 2: Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

    Prototype: def append_write(filename="", text=""):


Task 3: Write a function that returns the JSON representation of an object (string):

    Prototype: def to_json_string(my_obj)

Task 4: Write a function that returns an object (Python data structure) represented by a JSON string:

    Prototype: def from_json_string(my_str):

Task 5: Write a function that writes an Object to a text file, using a JSON representation:

    Prototype: def save_to_json_file(my_obj, filename):

Task 6: Write a function that creates an Object from a “JSON file”:

    Prototype: def load_from_json_file(filename):

Task 7: Write a script that adds all arguments to a Python list, and then save them to a file:

    You must use your function save_to_json_file from 5-save_to_json_file.py
    You must use your function load_from_json_file from 6-load_from_json_file.py
    The list must be saved as a JSON representation in a file named add_item.json

Task 8: Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

    Prototype: def class_to_json(obj):

Task 9: Write a class Student that defines a student by:

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)

Task 10: Write a class Student that defines a student by: (based on 9-student.py)
    If attrs is a list of strings, only attribute names contained in this list must be retrieved.Otherwise, all attributes must be retrieved

Task 11:Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py):

    Public method def reload_from_json(self, json): that replaces all attributes of the Student instance

Task 12: Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
