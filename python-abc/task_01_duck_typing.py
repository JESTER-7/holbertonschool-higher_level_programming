#!/usr/bin/python3
"""create an abstract class"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """abstract class shape"""

    @abstractmethod
    def area(self):
        """area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """perimeter of the shape"""
        pass


class Circle(Shape):
    """circle subclass"""

    def __init__(self, radius):
        """init"""
        self.radius = radius

    def area(self):
        """area method"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """perimeter method"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """rectangle subclass"""

    def __init__(self, width, height):
        """init"""
        self.width = width
        self.height = height

    def area(self):
        """area method"""
        return self.width * self.height

    def perimeter(self):
        """perimeter method"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """area and perimeter of the shape"""

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
