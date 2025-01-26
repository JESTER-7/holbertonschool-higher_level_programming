#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix1 = []
    for i in matrix:
        rowSquare = []
        for element in i:
            rowSquare.append(element ** 2)
        matrix1.append(rowSquare)
    return matrix1
