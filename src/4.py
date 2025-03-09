def calculate_sum(num1, num2):
    return num1 + num2

def calculate_subtraction(num1, num2):
    return num1 - num2

def calculate_multiplication(num1, num2):
    return num1 * num2

def calculate_division(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

def main():
    print("Welcome to the calculator! What would you like to do?")
    choice = input()
    while choice != "exit":
        if choice == "sum":
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            result = calculate_sum(num1, num2)
            print(f"The sum is {result}")
        elif choice == "subtraction":
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            result = calculate_subtraction(num1, num2)
            print(f"The subtraction is {result}")
        elif choice == "multiplication":
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            result = calculate_multiplication(num1, num2)
            print(f"The multiplication is {result}")
        elif choice == "division":
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            result = calculate_division(num1, num2)
            print(f"The division is {result}")
        else:
            print("Invalid choice")
        choice = input("What would you like to do? (sum, subtraction, multiplication, division or exit): ")
    print("Thank you for using the calculator!")
