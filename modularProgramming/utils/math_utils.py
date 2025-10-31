# Contains reusable mathematical functions.


def factorial(n):
    """Returns the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def gcd(a, b):
    """Finds the Greatest Common Divisor (GCD) using recursion."""
    if b == 0:
        return a
    return gcd(b, a % b)


def fibonacci(n):
    """Generates a Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
