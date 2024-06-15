#!/usr/bin/python3
""" 
contains the function matrix_divided(matrix, div)
"""
    
def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:
        matrix (int or float): matrix of intergers or floats to be divided
        div (int or float): divisor of matrix elements
    
    Return:
        new matrix of elements, to 2 decimal places.
    """
    
    if (not isinstance(div, (int, float))) or div is None or (div == float('inf') or div == float('-inf')) or div is float('nan'):
        raise TypeError ("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix " + "(list of lists) " + "of integers/floats")

    # if any((num == float('nan') for num in row) for row in matrix) or any((num == float('inf') or num == float('-inf') for num in row) for row in matrix):
    #     raise TypeError("matrix must be a matrix " + "(list of lists) " + "of integers/floats")
    
    # if any((num == float('nan') for num in row) for row in matrix):
    #     raise TypeError("matrix must be a matrix " + "(list of lists) " + "of integers/floats")
    
    # any(num == float('inf') or num == float('-inf'))):
    
    expected_row_size  = len(matrix[0])
    if any(len(row) != expected_row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    

    quotient = [[round(num / div, 2) for num in row] for row in matrix]

    return quotient
