#!/usr/bin/env python3

def get_factors(number, list_to_filter_by=[]):
    if not list_to_filter_by:
        list_to_filter_by = list(range(1, number+1))
    
    factors = []
    check_list = list_to_filter_by
    for check_number in list_to_filter_by:
        for multiply_number in check_list:
            if check_number * multiply_number == number:
                if check_number not in factors:
                    factors.append(check_number)
                break
    
    return factors