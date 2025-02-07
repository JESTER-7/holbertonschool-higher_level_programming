#!/usr/bin/python3
"""Create a class"""


class MyList(list):
    """define a class"""
    def print_sorted(self):
        sort1 = []
        for i in self:
            sort1.append(i)
        sort1.sort()
        print(sort1)
