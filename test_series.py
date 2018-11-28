from series import fibonacci
from series import lucas
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


def test_fibonacci_case_0():
    a = 0
    actual = 0
    assert fibonacci(a) == actual

def test_lucas_case_5():
    a = 5
    actual = 11
    assert lucas(a) == actual


def test_lucas_case_1():
    a = 1
    actual = 1
    assert lucas(a) == actual


def test_lucas_case_17():
    a = 17
    actual = 3571
    assert lucas(a) == actual


def test_lucas_case_99():
    a = 99
    actual = 489526700523968661124
    assert lucas(a) == actual


def test_lucas_case_0():
    a = 0
    actual = 2
    assert lucas(a) == actual

# fib = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
