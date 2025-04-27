import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def exponent(base, exp):
    return base ** exp

def square_root(num):
    return math.sqrt(num)

# Example usage
result = add(3, 5)
print(result)  # Output: 8
