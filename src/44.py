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
        return "Cannot divide by zero"

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def power(x, y):
    return x ** y

def round_number(num, decimal_places=2):
    return round(num, decimal_places)

def is_even(num):
    return num % 2 == 0
