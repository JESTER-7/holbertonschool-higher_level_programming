#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    romanNumber = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if len(roman_string) > i + 1 and roman_string[i] == "I":
            if roman_string[i + 1] == "V" or roman_string[i + 1] == "X":
                romanNumber -= 1
                continue
        romanNumber += roman[roman_string[i]]
    return romanNumber
