#!/usr/bin/python3
"""Create a class"""


class MyList(list):
    """define class"""
    def print_sorted(self):
        print(sorted(self))
