0x08. Python - More Classes and Objects 

Task 0: Write an empty class Rectangle that defines a rectangle:

Task 1: Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

    Private instance attribute: width:
        property def width(self): to retrieve it
        property setter def width(self, value): to set it:
    Private instance attribute: height:
        property def height(self): to retrieve it
        property setter def height(self, value): to set it:
    Instantiation with optional width and height: def __init__(self, width=0, height=0):

Task 2:Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

    Private instance attribute: width.
    Private instance attribute: height.
    Instantiation with optional width and height: def __init__(self, width=0, height=0):
    Public instance method: def area(self): that returns the rectangle area
    Public instance method: def perimeter(self): that returns the rectangle perimeter.

Task 3: Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)

    Public instance method: def area(self): that returns the rectangle area
    Public instance method: def perimeter(self): that returns the rectangle perimeter:

    if width or height is equal to 0, perimeter is equal to 0

You are not allowed to import any module

Task 4: Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
    repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()

Task 5: Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
    Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted

Task 6: Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)
    Public class attribute number_of_instances:
        Initialized to 0
        Incremented during each new instance instantiation
        Decremented during each instance deletion


Task 7: Write a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)
    Public class attribute print_symbol:
    Initialized to #
    Used as symbol for string representation
    Can be any type


Task 8: Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)
    Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
