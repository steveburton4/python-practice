#!/usr/bin/env python3

def get_prime_numbers(min_number, max_number):
    numbers = []
    for number in range(min_number, max_number):
        if number != 1 and number != 0:
            for check_number in range(2, number):
                if number % check_number == 0:
                    break
            else:
                numbers.append(number)
    return numbers