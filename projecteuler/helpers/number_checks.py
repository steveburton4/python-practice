#!/usr/bin/env python3

def is_palindromic_number(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")

    number_string = str(number)
    number_of_digits = len(number_string)
    if number_of_digits <= 1:
        return True

    halfway_digit = int(number_of_digits / 2)
    for count, char in enumerate(number_string):
        end_count = 0 - (count + 1)
        if (count <= halfway_digit) and (char != number_string[end_count]):
            return False
    
    return True;