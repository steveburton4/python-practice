#!/usr/bin/env python3

import pytest
from projecteuler.helpers import factors

def test_correct_factors_returned_for_ten():
    assert factors.get_factors(10) == [1, 2, 5, 10]

def test_correct_factors_returned_for_ten_with_filtered_list():
    assert factors.get_factors(10, [1, 2, 3, 5]) == [2, 5]