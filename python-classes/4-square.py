#!/usr/bin/python3
class Square:
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

    def area(self):
        """
        return the size
        """
        return self.__size ** 2
