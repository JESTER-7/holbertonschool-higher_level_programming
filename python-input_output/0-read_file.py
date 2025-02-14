#!/usr/bin/python3
"""file"""


def read_file(filename=""):
    """
    r = read only
    w = write only
    a = write at the end of the file
    x = read and write
    r+ = read and write in the same file
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
