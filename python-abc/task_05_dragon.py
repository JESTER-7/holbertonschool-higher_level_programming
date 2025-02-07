#!/usr/bin/python3
"""dragon can both swim AND fly."""


class SwimMixin:
    """class for the swim capacity"""

    def swim(self):
        """swim method"""
        print("The creature swims!")


class FlyMixin:
    """class for the fly capacity"""

    def fly(self):
        """fly method"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """dragon class"""

    def roar(self):
        """roar method"""
        print("The dragon roars!")
