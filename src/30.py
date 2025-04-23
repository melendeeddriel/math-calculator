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

# Example usage:
result1 = add(5, 3)
result2 = subtract(5, 3)
result3 = multiply(4, 6)
result4 = divide(10, 2)

print("Result of addition:", result1)
print("Result of subtraction:", result2)
print("Result of multiplication:", result3)
print("Result of division:", result4)
