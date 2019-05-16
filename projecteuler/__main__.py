#!/usr/bin/env python3

from projecteuler.problems import sums, finds

if __name__ == '__main__':
    print("Problem 1:", sums.get_sum_of_multiples_of_three_or_five(1000))
    print("Problem 2:", sums.get_sum_of_even_fibonacci_numbers(4000000))
    print("Problem 3:", finds.find_largest_prime_factor(13195))
    print("Problem 4:", finds.find_largest_palindromic_product(100, 999))
    print("Problem 5:", finds.find_smallest_multiple(1, 20))