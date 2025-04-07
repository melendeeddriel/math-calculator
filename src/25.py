def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b != 0:
        return a / b
    else:
        raise ValueError("Divide by zero error")

def calculate(expression: str) -> float:
    values = expression.split()
    operators = ["+", "-", "*", "/"]
    result = values[0]
    for i in range(1, len(values)):
        if operators.index(result[-1]) == operators.index(values[i][-1]):
            return None
        elif result[-1] != " ":  # check if it's a number
            current_value = ""
            while operators.index(current_value) <= operators.index(values[i]):
                current_value += values[i][operators.index(values[i]) + 1]
            else:
                current_value = values[i]
            result += current_value
    return float(result)

if __name__ == "__main__":
    expression = input("Enter an expression: ")
    try:
        print(f"Result: {calculate(expression)}")
    except ValueError as e:
        print(e)
