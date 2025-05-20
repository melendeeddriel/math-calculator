import math

def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Division by zero error"
    else:
        raise ValueError("Invalid operation")

print(calculate(5, 3, "add"))
print(calculate(5, 3, "subtract"))
print(calculate(5, 3, "multiply"))
print(calculate(5, 3, "divide"))
