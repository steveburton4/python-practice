#!/usr/bin/env python3

import math

def get_factors(number):
    factors = set()
    for check_number in range(1, int(math.sqrt(number))+1):
        if number % check_number == 0:
            factors.update({check_number, number // check_number})
    
    return factors