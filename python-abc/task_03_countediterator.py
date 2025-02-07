#!/usr/bin/python3
"""extends the built-in iterator obtained from the iter function"""


class CountedIterator:
    """extends the built-in iterator obtained from the iter function"""

    def __init__(self, iterable):
        """init"""
        self.iterator = iter(iterable)   # iterator from the iterable
        self.count = 0

    def __next__(self):
        """increment count with next method"""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration   # no items are left

    def get_count(self):
        """return the count"""
        return self.count
