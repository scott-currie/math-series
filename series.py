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


if __name__ == '__main__':
    print(', '.join([str(fibonacci(i)) for i in range(10)]))
    print(', '.join([str(lucas(i)) for i in range(10)]))
