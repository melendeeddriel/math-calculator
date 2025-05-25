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

print(add(2, 3))      # Output: 5
print(subtract(10, 5)) # Output: 5
print(multiply(4, 6))  # Output: 24
print(divide(7, 2))   # Output: 3.5
