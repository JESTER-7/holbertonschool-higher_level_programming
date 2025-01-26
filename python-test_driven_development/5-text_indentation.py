#!/usr/bin/python3


"""
print a text with 2 new lines after each of these characters: ., ? and :
text_indentation: same
exemple: ./5-main.py | cat -e
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :

    Parameter:
        text: the text to indentate

    Return:
        the new text
    """
    if isinstance(text, str):
        raise TypeError("text must be a string")
    newText = ""
    speChar = ['.', '?', ':']
    for char in text:
        newText += char
        if char in speChar:
            print(newText.strip())  # return a cpy of the str without space
            print()
            newText = ""
    if newText:  # if the string not end with ., ?, or :
        print(newText.strip())
