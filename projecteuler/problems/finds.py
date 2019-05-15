#!/usr/bin/env python3

from projecteuler.helpers import primenumbers, factors, number_checks

def find_largest_prime_factor(number):
    primes = primenumbers.get_prime_numbers(0, number)
    if not primes:
        return None
    
    all_factors = factors.get_factors(number)
    if not all_factors:
        return None

    prime_factors = set(primes).intersection(all_factors)
    return None if not prime_factors else max(prime_factors)

def find_largest_palindromic_sum(min_number_to_sum, max_number_to_sum):
    for max_number in range(max_number_to_sum, 0, -1):
        for min_number in range(max_number_to_sum, min_number_to_sum, -1):
            sum_number = max_number * min_number
            if number_checks.is_palindromic_number(sum_number):
                return sum_number
    return None

def find_smallest_multiple(min_number, max_number):
    if min_number <= 0 or max_number <= 0:
        raise TypeError("Min and max inputs must be positive whole numbers")
    
    count=1
    while(True):
        for divisible_number in range(min_number, max_number+1):
            if count % divisible_number != 0:
                break
        else:
            return count

        count += 1
    
    return None