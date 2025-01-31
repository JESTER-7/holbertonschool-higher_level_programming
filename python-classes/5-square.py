#!/usr/bin/python3
"""create the square class"""


class Square:
    """define the square class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        getter method
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        print a square with "#" char
        """
        if self.__size == 0:
            print("")
        for datSquare in range(self.__size):
            print("#" * self.__size)

    def area(self):
        """
        return the size
        """
        return self.__size ** 2
