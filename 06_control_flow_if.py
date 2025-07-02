"""
Python Workshop - 06: Control Flow - If Statements
==================================================

This file demonstrates Python conditional statements (if, elif, else).
"""

# 1. Basic if statement
age = 18
if age >= 18:
    print("You are an adult")

print("This line always executes\n")

# 2. if-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("It's not too hot")

# 3. if-elif-else statement
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# 4. Multiple conditions with logical operators
age = 25
has_license = True
has_car = False

# AND operator
if age >= 18 and has_license:
    print("You can legally drive")

# OR operator
if has_license or age >= 21:
    print("You meet at least one requirement")

# NOT operator
if not has_car:
    print("You don't have a car")

# Complex logical expressions
if age >= 18 and has_license and (has_car or age >= 21):
    print("You can drive and meet additional criteria")

# 5. Nested if statements
weather = "sunny"
temperature = 22

if weather == "sunny":
    if temperature > 20:
        print("Perfect day for outdoor activities!")
    else:
        print("Sunny but a bit cool")
else:
    if weather == "rainy":
        print("Stay inside")
    else:
        print("Check the weather again")

# 6. Comparison operators
x = 10
y = 5

print(f"\nComparison examples (x={x}, y={y}):")
if x == y:
    print("x equals y")
elif x != y:
    print("x does not equal y")

if x > y:
    print("x is greater than y")

if x >= y:
    print("x is greater than or equal to y")

if y < x:
    print("y is less than x")

if y <= x:
    print("y is less than or equal to x")

# 7. Membership operators
fruits = ["apple", "banana", "cherry"]
user_choice = "banana"

if user_choice in fruits:
    print(f"{user_choice} is available")
else:
    print(f"{user_choice} is not available")

# Using 'not in'
if "orange" not in fruits:
    print("Orange is not in the list")

# 8. Identity operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"\nIdentity examples:")
if a is c:
    print("a and c refer to the same object")

if a is not b:
    print("a and b are different objects (even with same content)")

if a == b:
    print("a and b have the same content")

# 9. Truthiness and Falsiness in Python
print(f"\nTruthiness examples:")

# Falsy values
if not 0:
    print("0 is falsy")

if not "":
    print("Empty string is falsy")

if not []:
    print("Empty list is falsy")

if not {}:
    print("Empty dict is falsy")

if not None:
    print("None is falsy")

# Truthy values
if 1:
    print("Non-zero numbers are truthy")

if "hello":
    print("Non-empty strings are truthy")

if [1, 2, 3]:
    print("Non-empty lists are truthy")

# 10. Conditional expressions (ternary operator)
age = 20
status = "adult" if age >= 18 else "minor"
print(f"\nAge: {age}, Status: {status}")

# More examples of ternary operator
x = 10
y = 5
max_value = x if x > y else y
print(f"Maximum of {x} and {y} is {max_value}")

# Nested ternary (not recommended for readability)
num = 0
result = "positive" if num > 0 else "negative" if num < 0 else "zero"
print(f"Number {num} is {result}")

# 11. Practical Examples

# User authentication system
username = "admin"
password = "secret123"
user_input = "admin"
pass_input = "secret123"

if user_input == username and pass_input == password:
    print("Login successful!")
elif user_input == username:
    print("Incorrect password")
elif pass_input == password:
    print("Incorrect username")
else:
    print("Invalid credentials")

# Grade calculator with validation
def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

test_scores = [95, 87, 76, 65, 52, -5, 105]
print(f"\nGrade calculations:")
for score in test_scores:
    grade = calculate_grade(score)
    print(f"Score {score}: Grade {grade}")

# Shopping cart discount system
def calculate_discount(total_amount, is_member, items_count):
    discount = 0
    
    if is_member:
        discount += 0.1  # 10% member discount
    
    if total_amount > 100:
        discount += 0.05  # 5% for orders over $100
    
    if items_count >= 5:
        discount += 0.03  # 3% for 5+ items
    
    # Maximum discount is 20%
    if discount > 0.2:
        discount = 0.2
    
    return discount

# Test the discount system
cart_scenarios = [
    (150, True, 6),   # Member, high amount, many items
    (80, True, 3),    # Member, low amount, few items
    (120, False, 4),  # Non-member, high amount, few items
    (50, False, 2),   # Non-member, low amount, few items
]

print(f"\nShopping cart discount examples:")
for amount, member, items in cart_scenarios:
    discount = calculate_discount(amount, member, items)
    final_amount = amount * (1 - discount)
    print(f"Amount: ${amount}, Member: {member}, Items: {items}")
    print(f"Discount: {discount*100:.1f}%, Final: ${final_amount:.2f}\n")

# 12. Input validation example
def validate_email(email):
    if not email:
        return False, "Email cannot be empty"
    elif "@" not in email:
        return False, "Email must contain @ symbol"
    elif email.count("@") != 1:
        return False, "Email must contain exactly one @ symbol"
    elif email.startswith("@") or email.endswith("@"):
        return False, "Email cannot start or end with @"
    elif ".." in email:
        return False, "Email cannot contain consecutive dots"
    else:
        return True, "Valid email"

# Test email validation
test_emails = [
    "user@example.com",
    "invalid.email",
    "@invalid.com",
    "user@@example.com",
    "",
    "user@.com",
    "user..name@example.com"
]

print(f"Email validation examples:")
for email in test_emails:
    is_valid, message = validate_email(email)
    status = "✓" if is_valid else "✗"
    print(f"{status} {email}: {message}")

# 13. Short-circuit evaluation
print(f"\nShort-circuit evaluation examples:")

def expensive_function():
    print("This expensive function was called")
    return True

# In AND, if first condition is False, second is not evaluated
x = 5
if x > 10 and expensive_function():
    print("Both conditions true")
else:
    print("First condition was false, so expensive_function was not called")

# In OR, if first condition is True, second is not evaluated
if x > 0 or expensive_function():
    print("First condition was true, so expensive_function was not called")

# 14. Common patterns and best practices
print(f"\nBest practices examples:")

# Use 'in' for multiple comparisons
day = "Saturday"
if day in ["Saturday", "Sunday"]:
    print("It's weekend!")

# Avoid deep nesting with early returns
def process_user(user_data):
    if not user_data:
        return "No user data provided"
    
    if "name" not in user_data:
        return "Name is required"
    
    if "age" not in user_data:
        return "Age is required"
    
    if user_data["age"] < 0:
        return "Age must be positive"
    
    # Main processing logic here
    return f"Processing user: {user_data['name']}"

# Test the function
test_users = [
    {},
    {"name": "Alice"},
    {"name": "Bob", "age": -5},
    {"name": "Charlie", "age": 25}
]

for user in test_users:
    result = process_user(user)
    print(f"User {user}: {result}")
