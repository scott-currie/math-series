def fibonacci(n):
    """Takes an int n as parameter and returns the nth Fibonacci number using an iterative method.
    """
    if n == 0:
        return 0
    fib = 1
    prev = 0
    for _ in range(1, n):
        tmp = fib
        fib += prev
        prev = tmp
    return fib

def lucas(n):
    """Takes an int n as parameter and returns the nth Lucas number using an iterative method.
    """
    if n == 0:
        return 2
    luc = 1
    prev = 2
    for _ in range(1, n):
        tmp = luc
        luc += prev
        prev = tmp
    return luc


def sum_series(n, n1=0, n2=1):
    """Takes an int n as parameter and 2 optional parameters and returns the nth number in sequence using an iterative method. The optional parameters determine the two starting values for the sequence.
    """
    if n == 0:
        return n1
    ss = n2
    prev = n1
    for _ in range(1, n):
        tmp = ss
        ss += prev
        prev = tmp
    return ss


if __name__ == '__main__':
    print('This module defines functions that implement mathematical series.')
    print('...')
    print('\nfibonacci(n):\n\n\tReturns the nth value in the fibonacci series.\n')
