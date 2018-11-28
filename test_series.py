from series import fibonacci
import pytest

def test_fibonacci_exists():
    assert fibonacci


def test_fibonacci_case_5():
    a = 5
    actual = 5
    assert fibonacci(a) == actual


def test_fibonacci_case_1():
    a = 1
    actual = 1
    assert fibonacci(a) == actual


def test_fibonacci_case_17():
    a = 17
    actual = 1597
    assert fibonacci(a) == actual


def test_fibonacci_case_99():
    a = 99
    actual = 218922995834555169026
    assert fibonacci(a) == actual


# fib = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
