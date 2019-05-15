#!/usr/bin/env python3

import pytest
from projecteuler.helpers import number_checks

@pytest.mark.parametrize("input_value", ["1", 2.1])
def test_is_palindronic_number_input_type(input_value):
    with pytest.raises(TypeError):
        number_checks.is_palindromic_number(input_value)

@pytest.mark.parametrize("number, result", [
    (11, True),
    (1, True),
    (7667, True),
    (76467, True),
    (12, False),
    (76447, False),
    (1667, False)
])
def test_is_palindronic_number(number, result):
    assert number_checks.is_palindromic_number(number) == result