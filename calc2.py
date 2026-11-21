print("Hello, feel free  to use this calculator for anything.")
print("First, let's calculate the sum")
def add(a, b):
    return a + b
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = add(a, b)
    print("The sum is", result)
except ValueError:
    print("Please enter valid integers.")
print("Next, let's calculate the difference")
def subtract(a, b):
    return a - b
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = subtract(a, b)
    print("The difference is", result)
except ValueError:
    print("Please enter valid integers.")
print("Now, let's calculate the product")
def multiply(a, b):
    return a * b
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = multiply(a, b)
    print("The product is", result)
except ValueError:
    print("Please enter valid integers.")
print("Finally, let's calculate the quotient")
def divide(a, b):
    return a / b
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = divide(a, b)
    print("The quotient is", result)
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")