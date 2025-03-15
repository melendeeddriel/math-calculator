  def add(a, b):
    return a + b

  def subtract(a, b):
    return a - b

  def multiply(a, b):
    return a * b

  def divide(a, b):
    if b == 0:
      raise ValueError("Cannot divide by zero")
    return a / b

  def remainder(a, b):
    if b == 0:
      raise ValueError("Cannot take remainder of a number with respect to zero")
    return a % b

  def power(a, b):
    return a ** b

  def square_root(a):
    if a < 0:
      raise ValueError("Square root of negative numbers is not supported")
    return a ** 0.5