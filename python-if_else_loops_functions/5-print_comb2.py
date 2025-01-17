#!/usr/bin/python3
for i in range(100):
    if i < 99:
        print("{:02}, ".format(i), end="")  # :02 = 2 digit
    else:
        print("{:02}".format(i))
