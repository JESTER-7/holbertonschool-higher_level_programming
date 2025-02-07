#!/usr/bin/python3
"""same as the 2"""


def inherits_from(obj, a_class):
    """same as the 2"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
