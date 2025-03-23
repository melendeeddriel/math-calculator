def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    else:
        return x / y

# Example usage
print("5 + 3 = ", add(5, 3))
print("10 - 2 = ", subtract(10, 2))
print("4 * 6 = ", multiply(4, 6))
print("7 // 2 = ", divide(7, 2))
