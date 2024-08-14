Python - Inheritance 

Task 0: Write a function that returns the list of available attributes and methods of an object

Task 1: Write a class MyList that inherits from list:

    Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)

Task 2: Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

Task 3: Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

Task 4: Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

Task 5: Write an empty class BaseGeometry.

Task 6: Write a class BaseGeometry (based on 5-base_geometry.py).

    Public instance method: def area(self): that raises an Exception with the message area() is not implemented

Task 7: Write a class BaseGeometry (based on 6-base_geometry.py).
    Public instance method: def integer_validator(self, name, value): that validates value:
        you can assume name is always a string
        if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
