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
        return "Error: Division by zero is not allowed."

def power(x, y):
    return x ** y

def square_root(x):
    return x ** 0.5

# Example usage:
result_add = add(5, 3)
result_subtract = subtract(10, 4)
result_multiply = multiply(2, 7)
result_divide = divide(8, 2)
result_power = power(2, 3)
result_sqrt = square_root(9)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")
print(f"Power: {result_power}")
print(f"Sqrt: {result_sqrt}")
