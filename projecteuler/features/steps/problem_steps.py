#!/usr/bin/env python3

from behave import given, when, then, step
from problems import sums

@given('the number {max_number:d}')
def step_impl(context, max_number):
    context.max_number = max_number

@when('I search for the sum of the multiples of 3 and 5')
def step_impl(context):
    context.result = sums.get_sum_of_even_fibonacci_numbers(context.max_number)
    
@then('I get {check_result:d}')
def step_impl(context, check_result):
    assert context.failed is False
    assert context.result == check_result