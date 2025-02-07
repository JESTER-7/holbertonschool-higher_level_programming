#!/usr/bin/python3
"""create a class"""


class BaseGeometry:
    """define a class"""

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate a value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """define a class"""

    def __init__(self, width, height):
        """define the init class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """change str rule"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """add area"""
        return self.__width * self.__height
