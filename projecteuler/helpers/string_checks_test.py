#!/usr/bin/env python3

import pytest
from projecteuler.helpers import string_checks

@pytest.mark.parametrize("input_string, result", [
    ("11", True),
    ("1", True),
    ("7667", True),
    ("76467", True),
    ("12", False),
    ("76447", False),
    ("1667", False)
])
def test_is_palindronic_number(input_string, result):
    assert string_checks.is_palindrome(input_string) == result