def fibonacci(n):
    """Find nth fibonacci number using recursive algorithm.

    input: n (int) n for nth fibonacci number
    returns: (int) representing value of nth fib number
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Find nth lucas number using recursive algorithm.

    input: n (int) n for nth lucas number
    returns: (int) representing value of nth lucas number
    """
    if n < 1:
        return 2
    elif n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, n1=0, n2=1):
    """Find nth value in a mathematical series, starting with 2 arbitrary numbers.

    input: n (int) n for nth value in sequence
    input: n1 (int) optional, represents val at sequence n=0
    input: n2 (int) optional, represents val at sequence n=1
    returns: (int) representing value at sequence n
    """
    if n < 1:
        return n1
    elif n == 1:
        return n2
    return sum_series(n - 1, n1, n2) + sum_series(n - 2, n1, n2)


if __name__ == '__main__':
    print('This module defines functions that implement mathematical series.')
    print('...')
    print('\nfibonacci(n):\n\n\tReturns the nth value in the fibonacci series.\n')
