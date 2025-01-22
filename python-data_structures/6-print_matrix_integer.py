#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i, element in enumerate(line):
            if i < len(line) - 1:
                print("{:d}".format(element), end=" ")
            else:
                print("{:d}".format(element), end="")
        print()
