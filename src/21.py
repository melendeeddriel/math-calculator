import math

def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b

# Example usage:
result = calculate(4, 2, "add")
print("Result of addition:", result)
