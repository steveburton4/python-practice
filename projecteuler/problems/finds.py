#!/usr/bin/env python3

from projecteuler.helpers import primenumbers, factors, string_checks

def find_largest_prime_factor(number):
    primes = primenumbers.get_prime_numbers(0, number)
    if not primes:
        return None
    
    all_factors = factors.get_factors(number)
    if not all_factors:
        return None

    prime_factors = set(primes).intersection(all_factors)
    return None if not prime_factors else max(prime_factors)

def find_largest_palindromic_product(min_number_to_sum, max_number_to_sum):
    for max_number in range(max_number_to_sum, 0, -1):
        for min_number in range(max_number_to_sum, min_number_to_sum, -1):
            sum_number = max_number * min_number
            if string_checks.is_palindrome(str(sum_number)):
                return sum_number
    return None

def find_smallest_multiple(min_number, max_number):
    if not isinstance(min_number, int) or not isinstance(max_number, int):
        raise ValueError("Min and max inputs must be positive whole numbers")

    if min_number <= 0 or max_number <= 0:
        raise ValueError("Min and max inputs must be positive whole numbers")

    if max_number < min_number:
        raise ValueError("Max number must be greater than or equal to min number")
    
    total = 1
    for number in range(min_number, max_number + 1):
        lowest_multiplier = 1
        for multiplier in range(1, number+1):
            if total * multiplier % number == 0:
                lowest_multiplier = multiplier
                break
        total *= lowest_multiplier

    return total