def calculate(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError("Only integers are allowed")
    return num1 + num2
