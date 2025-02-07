#!/usr/bin/python3
"""fish and bird classes"""


class Fish:
    """fish class"""

    def swim(self):
        """swim method"""
        print("The fish is swimming")

    def habitat(self):
        """habitat method"""
        print("The fish lives in water")


class Bird:
    """bird class"""

    def fly(self):
        """fly method"""
        print("The bird is flying")

    def habitat(self):
        """habitat method"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """flyingfish class"""

    def habitat(self):
        """habitat method"""
        print("The flying fish lives both in water and the sky!")

    def swim(self):
        """swim method"""
        print("The flying fish is swimming!")

    def fly(self):
        """fly method"""
        print("The flying fish is soaring!")
