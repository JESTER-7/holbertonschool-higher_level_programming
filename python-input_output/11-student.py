#!/usr/bin/python3
"""file"""


class Student:
    """student class with attributes"""
    
    def __init__(self, first_name, last_name, age):
        """init method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """retrieve a dict repr of a student instance"""

        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list):
            dict = {}
            for i in attrs:
                # Return whether the object has an attribute with the given name
                if isinstance(i, str) and hasattr(self, i):
                    dict[i] = getattr(self, i)  # get a named attribute from an object
                return dict
        else:
            return self.__dict__
    
    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for i in json:
                self.__dict__[i] = json[i]
