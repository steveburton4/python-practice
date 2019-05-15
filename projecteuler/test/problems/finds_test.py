#!/usr/bin/env python3

import pytest
from projecteuler.problems import finds

@pytest.mark.parametrize("input_value, result", [
    (0, None),
    (6, 3),
    (10, 5)
])
def test_find_prime_factors_for_input_zero(input_value, result):
    assert finds.find_largest_prime_factor(input_value) == result

@pytest.mark.parametrize("min_input, max_input, result", [
    (10, 99, 9009),
    (1, 11, 121),
    (10, 11, 121)
])
def test_find_largest_palindromic_number(min_input, max_input, result):
    assert finds.find_largest_palindromic_product(min_input, max_input) == result

@pytest.mark.parametrize("min_input, max_input, result", [
    (1, 10, 2520),
    (1, 2, 2),
    (2, 5, 60)
])
def test_find_smallest_multiple(min_input, max_input, result):
    assert finds.find_smallest_multiple(min_input, max_input) == result

@pytest.mark.parametrize("min_input, max_input", [
    (0, 1),
    (1, 0),
    (2, 1),
    ("1", 2),
    (1, "2"),
    (None, 1),
    (1, None)
])
def test_find_smallest_multiple_input_values(min_input, max_input):
    with pytest.raises(ValueError):
        finds.find_smallest_multiple(min_input, max_input)