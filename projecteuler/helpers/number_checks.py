#!/usr/bin/env python3

def is_palindrome(input_string):
    for start_index in range(0, len(input_string) // 2):
        end_index = 0 - start_index - 1
        if input_string[start_index] != input_string[end_index]:
            return False
    
    return True;