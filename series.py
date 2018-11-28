def fibonacci(n):
    """Takes an int n as parameter and returns the nth Fibonacci number using an iterative method.
    """
    fib = 1
    prev = 1
    for _ in range(2, n):
        tmp = fib
        fib += prev
        prev = tmp
    return fib

if __name__ == '__main__':
    fibonacci(5)
