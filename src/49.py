def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

# Test the functions with some data points
print(add(10, 5))         # Output: 15
print(subtract(10, 5))     # Output: 5
print(multiply(10, 5))    # Output: 50
print(divide(10, 5))      # Output: 2.0
