#!/usr/bin/python3
"""return true or false"""


def is_same_class(obj, a_class):
    """same"""
    if a_class is type(obj):
        return True
    else:
        return False
