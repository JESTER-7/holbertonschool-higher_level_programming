#!/usr/bin/python3


"""
print the full name
say_my_name: print a name
exemple: print(say_my_name("Walter", "White"))
"""


def say_my_name(first_name, last_name=""):
    """
    print "My name is <first_name> <last_name>"
    
    Parameter:
        first_name: first name
        last_name: last name
    
    Return:
        a full name or not if there is no last_name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
