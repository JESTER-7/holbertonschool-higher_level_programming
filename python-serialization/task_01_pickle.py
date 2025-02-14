#!/usr/bin/env python3
"""custom objet class"""

import pickle


class CustomObject:
    """custom objet class"""

    def __init__(self, name, age, is_student):
        """init method"""

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """display the object's attributes"""

        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the current instance and save it to a file"""
        try:
            with open(filename, 'wb', encoding="utf-8") as file:
                pickle.dump(self, file)
        except (FileNotFoundError, pickle.PickleError, EOFError) as e:
            print("Error serializing object: {}".format(e))
            return None

    @classmethod
    def deserialize(cls, filename):
        """deserialize a class instance from a file"""

        try:
            with open(filename, 'rb', encoding="utf-8") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError) as e:
            print("Error deserializing object: {}".format(e))
            return None
