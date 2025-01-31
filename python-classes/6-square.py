#!/usr/bin/python3
"""create the square class"""


class Square:
    """define the square class"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        getter method for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method for size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        getter method for position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter method for position
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        print a square with "#" char
        """
        if self.__size == 0:
            print("")
        for datSquare in range(self.__size):
            if self.__position[0] != 0:
                print(" " * (self.__position[0] - 1), "#" * self.__size)
            else:
                print("#" * self.__size)

    def area(self):
        """
        return the size
        """
        return self.__size ** 2
