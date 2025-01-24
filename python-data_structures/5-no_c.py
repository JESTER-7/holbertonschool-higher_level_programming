#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for remove in my_string:
        if remove not in "cC":
            result += remove
    return result
