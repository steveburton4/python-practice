#!/usr/bin/env python3

import pytest
from projecteuler.helpers import primenumbers

@pytest.mark.parametrize("min, max, result", [
    (1, 10, [2, 3, 5, 7]),
    (-1, -10, []),
    (10, 1, [])
])
def test_correct_prime_numbers_returned(min, max, result):
    assert primenumbers.get_prime_numbers(min, max) == result