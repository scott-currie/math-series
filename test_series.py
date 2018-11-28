from series import fibonacci
import pytest

def test_fibonacci_exists():
    assert fibonacci

def test_fibonacci_case_1():
    a = 5
    actual = 5
    assert fibonacci(a) == actual


# fib = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
