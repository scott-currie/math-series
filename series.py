def fibonacci(n):
    """Takes an int n as parameter and returns the nth Fibonacci number using an iterative method.
    """
    p1 = 1
    p2 = 1
    fib = 0
    for _ in range(n + 1):
        tmp = fib
        fib = p1 + p2
        p1 = p2
        p2 = tmp
    return fib
