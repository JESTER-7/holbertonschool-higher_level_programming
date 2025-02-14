#!/usr/bin/python3
"""file"""


def write_file(filename="", text=""):
    """write in a file"""

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
