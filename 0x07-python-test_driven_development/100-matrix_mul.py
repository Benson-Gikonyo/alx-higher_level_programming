#!/usr/bin/python3
"""defines matrix_mul function"""


def transpose(matrix):
    """ transpose matrix """
    new_matrix = []
    for column in matrix[0]:
        new_matrix.append([])
    for row in matrix:
        for index, item in enumerate(row):
            new_matrix[index].append(item)
    return new_matrix


def calc_product(row_a, row_b):
    """ calculate individual index of new matrix """
    sum = 0
    for index, item in enumerate(row_a):
        sum += item * row_b[index]
    return sum


def mult(m_a, m_b):
    """ multiply a matrix """
    t_b = transpose(m_b)
    new_matrix = []
    for row in m_a:
        new_matrix.append([])
    result = 0
    for index_a, row_a in enumerate(m_a):
        for index_b, row_b in enumerate(t_b):
            result = calc_product(row_a, row_b)
            new_matrix[index_a].append(result)
    return new_matrix


def matrix_mul(m_a, m_b):
    """multiply 2 matrices

    Args:
        m_a (list): matrix 1
        m_b (list): matrix 2
    """
    # are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # are nested lists
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    # are empty lists
    if m_a == []:
        raise ValueError("m_a can't be empty")
    for row in m_a:
        if row == []:
            raise ValueError("m_a can't be empty")

    if m_b == []:
        raise ValueError("m_b can't be empty")
    for row in m_b:
        if row == []:
            raise ValueError("m_b can't be empty")

    for row in m_a:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("m_b should contain only integers or floats")

    # rows are same size
    expected_row_size_1 = len(m_a[0])
    expected_row_size_2 = len(m_b[0])

    for row in m_a:
        if len(row) != expected_row_size_1:
            raise TypeError("Each row of m_a must have the same size")

    for row in m_b:
        if len(row) != expected_row_size_2:
            raise TypeError("Each row of m_b must have the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return mult(m_a, m_b)
