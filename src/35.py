import math

def calculate(a, b):
    """
    This function performs basic mathematical operations: addition, subtraction,
    multiplication, and division.
    
    :param a: The first number
    :type a: float or int
    :param b: The second number
    :type b: float or int
    :return: The result of the calculation
    :rtype: float or int
    """
    return (a + b) / 2.0

def main():
    while True:
        user_input = input("Enter a, b and operation (+, -, *, /): ")
        
        if user_input == "q":
            print("Exiting the program...")
            break
        
        if user_input.isdigit():
            a, b = map(float, user_input.split(','))
            
            result = calculate(a, b)
            
            print(f"Result: {result}")

if __name__ == "__main__":
    main()
