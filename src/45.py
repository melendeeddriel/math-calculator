import math
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Error: Division by zero is not allowed.")
    return x / y

print(add(10, 2))   # Output: 12
print(subtract(10, 2)) # Output: 8
print(multiply(10, 2)) # Output: 20
print(divide(10, 2)) # Output: 5.0
