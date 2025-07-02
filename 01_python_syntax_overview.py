"""
Python Workshop - 01: Python Syntax Overview
============================================

This file demonstrates basic Python syntax fundamentals.
"""

# 1. Comments
# This is a single-line comment

"""
This is a multi-line comment
or docstring that can span
multiple lines
"""

# 2. Variables and Basic Assignment
name = "Python Workshop"
year = 2025
pi = 3.14159
is_awesome = True

print(f"Welcome to {name} in {year}!")
print(f"Pi value: {pi}")
print(f"Is Python awesome? {is_awesome}")

# 3. Print statements and string formatting
print("Hello, World!")  # Basic print
print("Name:", name)    # Multiple values
print(f"Year: {year}")  # f-string formatting
print("Pi is approximately {:.2f}".format(pi))  # .format() method

# 4. Input from user
# user_name = input("What's your name? ")
# print(f"Nice to meet you, {user_name}!")

# 5. Multiple assignment
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# 6. Basic arithmetic operators
a = 10
b = 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# 7. Comparison operators
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# 8. Logical operators
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# 9. Basic functions
def greet(name, age=25):
    """A simple function with a default parameter"""
    return f"Hello, {name}! You are {age} years old."

def add_numbers(x, y):
    """Function that adds two numbers"""
    return x + y

# Function calls
print(greet("Alice"))
print(greet("Bob", 30))
print(f"Sum: {add_numbers(5, 7)}")

# 10. Indentation (Python's way of defining code blocks)
if True:
    print("This is properly indented")
    if True:
        print("This is nested indentation")
    print("Back to first level")

print("This is at the root level")
