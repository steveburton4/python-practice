#!/usr/bin/env python3

import math

def get_prime_numbers(min_number, max_number):
    primes = []
    for possibleprime in range(min_number, max_number):
        if possibleprime > 1:
            if all(possibleprime % check_number != 0 for check_number in range(2, math.trunc(math.sqrt(possibleprime)) + 1)):
                primes.append(possibleprime)
    return primes