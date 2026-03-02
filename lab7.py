# lab7.py

# Solutions for assignments about functions, scope, and recursion

# 1. Function examples

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

print("Addition of 5 and 3:", add(5, 3))


def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

print("Multiplication of 5 and 3:", multiply(5, 3))


# 2. Scope examples

x = 10  # Global variable

def local_scope_example():
    y = 5  # Local variable
    print("Inside local_scope_example, y:", y)

local_scope_example()
print("Outside function, x:", x)


# 3. Recursive function examples

# Factorial

def factorial(n):
    """Returns the factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# Fibonacci

def fibonacci(n):
    """Returns the n-th Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci of 6:", fibonacci(6))
