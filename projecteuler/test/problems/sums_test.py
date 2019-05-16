#!/usr/bin/env python3

import pytest
from projecteuler.problems import sums

@pytest.mark.parametrize("input_value, result", [
    (0, 0),
    (10, 23),
    (3, 0),
    (4, 3),
    (6, 8)
])
def test_sum_of_multiples_three_and_five_for_input_zero(input_value, result):
    assert sums.get_sum_of_multiples_of_three_or_five(input_value) == result

@pytest.mark.parametrize("input_value, result", [
    (10, 10),
    (0, 0),
    (1, 0),
    (100, 44)
])
def test_sum_of_even_fibonacci_numbers_for_input_ten(input_value, result):
    assert sums.get_sum_of_even_fibonacci_numbers(input_value) == result