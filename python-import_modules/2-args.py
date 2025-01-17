#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenArgv = len(argv)
    if lenArgv > 2:
        string = "arguments:"  # if 2 or more arguments
    if lenArgv == 1:
        string = "arguments."  # if no arguments
    if lenArgv == 2:
        string = "argument:"   # if 1 argument
    print("{} {}".format(lenArgv - 1, string))
    for i in range(1, lenArgv):
        print("{}: {}".format(i, argv[i]))
