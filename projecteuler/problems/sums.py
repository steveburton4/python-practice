#!/usr/bin/env python3

def get_sum_of_multiples_of_three_or_five(maximum_number):
    result = 0
    for count in range(1, maximum_number):
        if count % 3 == 0 or count % 5 == 0:
            result += count
    return result

def get_sum_of_even_fibonacci_numbers(maximum_number):
    current_number, last_number, next_number = 1, 1, 2
    result = 0
    while (current_number < maximum_number):
        if current_number % 2 == 0:
            result += current_number

        last_number = current_number
        current_number = next_number
        next_number = current_number + last_number
    return result