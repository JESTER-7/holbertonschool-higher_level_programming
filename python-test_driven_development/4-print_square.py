#!/usr/bin/python3


"""
print some squares
print_square: print sqaures
exemple: print_square(20)
"""


def print_square(size):
    """
    Print a square with the character '#'
    
    Parameter:
        size: len of the square
    
    Return:
        a square
    """
    if type(size) is not int:
        if type(size) is float:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
