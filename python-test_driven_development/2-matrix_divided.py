#!/usr/bin/python3


"""
divide elements of a matrix
matrix_divided: function to divide elements in a matrix
exemple: print(matrix_divided(matrix, 3))
"""


def matrix_divided(matrix, div):
    """
    divides all elements in a matrix by div

    Parameter:
        matrix: listx2 of int or float
        div: divide

    Return:
        new matrix with all elements divided by div
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    rowLength = len(matrix[0])
    for row in matrix:
        if len(row) != rowLength:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    newMatrix = []
    for row in matrix:
        newRow = []
        for num in row:
            newRow.append(round(num / div, 2))  # round to 2 decimal places
        newMatrix.append(newRow)
    return newMatrix
