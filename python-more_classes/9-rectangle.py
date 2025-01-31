#!/usr/bin/python3
"""create the rectangle class"""


class Rectangle:
    """define the rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        getter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter method for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        return the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        return the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") * self.height)\
            .strip()
        # strip remove the last line

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        static method belong to a class, not it's instance
        we use it here because we don't need to modify with the instence self,
        it operate purely on the arguments
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():  # area of the rect
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        the class method define a method that is bound to the
        class and not the instance
        we use it here because we want to create a new instance of rectangle
        """
        return cls(width=size, height=size)
