import math

def calculate(num1, num2, operator):
    if operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2
    elif operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return num1 / num2

# Example usage:
result = calculate(5, 3, "add")
print("The result is:", result)

result = calculate(5, 3, "subtract")
print("The result is:", result)

result = calculate(5, 3, "multiply")
print("The result is:", result)

result = calculate(5, 3, "divide")
print("The result is:", result)
