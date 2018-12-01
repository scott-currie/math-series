from series import fibonacci
from series import lucas
from series import sum_series
import pytest


def test_fibonacci_exists():
    assert fibonacci

# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def test_fibonacci_case_5():
    """Test fibonacci function with n and known result
    """
    a = 5
    actual = 5
    assert fibonacci(a) == actual


def test_fibonacci_case_1():
    """Test fibonacci function with n and known result
    """
    a = 1
    actual = 1
    assert fibonacci(a) == actual


def test_fibonacci_case_17():
    """Test fibonacci function with n and known result
    """
    a = 17
    actual = 1597
    assert fibonacci(a) == actual


# def test_fibonacci_case_39():
#     """Test fibonacci function with n and known result
#     """
#     a = 39
#     actual = 63245986
#     assert fibonacci(a) == actual


def test_fibonacci_case_0():
    """Test fibonacci function with n and known result
    """
    a = 0
    actual = 0
    assert fibonacci(a) == actual

# Lucas: 2, 1, 3, 4, 7, 11, 18, 29, 47, 76

def test_lucas_case_5():
    """Test lucas function with n and known result
    """
    a = 5
    actual = 7
    assert lucas(a) == actual


def test_lucas_case_1():
    """Test lucas function with n and known result
    """
    a = 1
    actual = 1
    assert lucas(a) == actual


def test_lucas_case_0():
    """Test lucas function with n and known result
    """
    a = 0
    actual = 2
    assert lucas(a) == actual


def test_lucas_case_5():
    """Test lucas function with n and known result
    """
    a = 5
    actual = 11
    assert lucas(a) == actual

def test_sum_series_fib():
    """Test whether sum_series gives fibonacci results here.
    """
    a = 17
    actual = 1597
    assert sum_series(a) == actual


def test_sum_series_lucas():
    """Test whether sum_series gives lucas results here.
    """
    a = 17
    actual = 3571
    assert sum_series(a, 2, 1) == actual


def test_sum_series_5_7():
    """Test sum_series with some arbitrary starting values
    """
    a = 5
    actual = 50
    assert sum_series(a, 5, 7) == actual

# 5 7 12 19 31
