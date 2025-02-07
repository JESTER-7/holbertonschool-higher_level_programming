#!/usr/bin/python3
"""abc abstract class"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """animal class"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """bark"""
    def __init__(self):
        """init"""
        self.soundDog = "Bark"

    def sound(self):
        """bark"""
        return self.soundDog


class Cat(Animal):
    """meow"""
    def __init__(self):
        """init"""
        self.soundCat = "Meow"

    def sound(self):
        """meow"""
        return self.soundCat
