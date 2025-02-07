#!/usr/bin/python3
"""create an ABC abstract class"""


class VerboseList(list):
    """create an abstract class"""

    def append(self, item):
        """append method"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """extend method"""
        items_added = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        """remove method"""
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        """pop method"""
        if self:
            item = self[index]
            print(f"Popped [{item}] from the list.")
            return super().pop(index)
        else:
            print("Cannot pop from an empty list.")
            raise IndexError("pop from empty list")
