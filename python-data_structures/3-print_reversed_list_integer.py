#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for list in my_list:
        print("{:d}".format(list[-my_list]))
