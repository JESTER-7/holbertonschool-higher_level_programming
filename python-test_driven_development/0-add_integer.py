#!/usr/bin/python3
"""
Add 2 integer
add_integer is the function to add integers
exemple: print(add_integer(4, 6))
"""
def add_integer(a, b=98):
    """
    Add 2 integers
    
    Parameter:
        a: first int
        b: second int
    
    Return:
        a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
