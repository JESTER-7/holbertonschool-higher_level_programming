#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return (0, None)
    int(my_list)
    for i in range len(my_list):
        if my_list[i] > my_list[i + 1]:
            return my_list[i]
        else:
            return my_list[i + 1]
