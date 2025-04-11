import math

def calculate_square_root(num):
    """Calculate square root of a number."""
    return math.sqrt(num)

def main():
    num = float(input("Enter a number: "))
    result = calculate_square_root(num)
    print(f"The square root of {num} is {result}")

if __name__ == "__main__":
    main()
