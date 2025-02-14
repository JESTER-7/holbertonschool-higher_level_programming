#!/usr/bin/python3
"""file"""


def append_write(filename="", text=""):
    """append text in a file"""

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
