"""
Python Workshop - 07: Control Flow - For Loops
==============================================

This file demonstrates Python for loops and their various uses.
"""

# 1. Basic for loop with range
print("Basic for loop with range:")
for i in range(5):
    print(f"Iteration {i}")

print()

# 2. For loop with different range parameters
print("Range with start, stop, step:")
for i in range(2, 10, 2):  # start=2, stop=10, step=2
    print(f"Even number: {i}")

print()

# Counting backwards
print("Counting backwards:")
for i in range(10, 0, -1):
    print(f"Countdown: {i}")

print()

# 3. Iterating over lists
fruits = ["apple", "banana", "cherry", "date"]
print("Iterating over a list:")
for fruit in fruits:
    print(f"I like {fruit}")

print()

# 4. Iterating with enumerate (getting index and value)
print("Using enumerate to get index and value:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print()

# Starting enumerate from a different number
print("Enumerate starting from 1:")
for number, fruit in enumerate(fruits, 1):
    print(f"{number}. {fruit}")

print()

# 5. Iterating over strings
word = "Python"
print(f"Iterating over string '{word}':")
for char in word:
    print(f"Character: {char}")

print()

# 6. Iterating over dictionaries
student = {"name": "Alice", "age": 25, "grade": "A", "city": "New York"}

print("Iterating over dictionary keys:")
for key in student:
    print(f"Key: {key}")

print()

print("Iterating over dictionary values:")
for value in student.values():
    print(f"Value: {value}")

print()

print("Iterating over dictionary key-value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

print()

# 7. Nested loops
print("Nested loops - Multiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        product = i * j
        print(f"{i} x {j} = {product}")
    print()  # Empty line after each row

# 8. Loop control statements

# Break statement
print("Using break to exit loop early:")
for i in range(10):
    if i == 5:
        print(f"Breaking at {i}")
        break
    print(f"Current number: {i}")

print()

# Continue statement
print("Using continue to skip iterations:")
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(f"Odd number: {i}")

print()

# 9. For-else construct
print("For-else construct (else executes if loop completes normally):")
for i in range(5):
    print(f"Processing {i}")
else:
    print("Loop completed successfully")

print()

print("For-else with break (else doesn't execute):")
for i in range(5):
    if i == 3:
        print("Breaking early")
        break
    print(f"Processing {i}")
else:
    print("This won't be printed because of break")

print()

# 10. List comprehensions (alternative to for loops)
print("Traditional for loop to create a list:")
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Squares: {squares}")

print("List comprehension (more Pythonic):")
squares_comp = [i ** 2 for i in range(1, 6)]
print(f"Squares: {squares_comp}")

print()

# List comprehension with condition
print("List comprehension with condition:")
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(f"Even squares: {even_squares}")

print()

# 11. Dictionary comprehensions
print("Dictionary comprehension:")
square_dict = {i: i ** 2 for i in range(1, 6)}
print(f"Square dictionary: {square_dict}")

print()

# 12. Iterating over multiple lists with zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

print("Using zip to iterate over multiple lists:")
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

print()

# Handling lists of different lengths
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30]

print("Zip with different length lists (stops at shortest):")
for a, b in zip(numbers1, numbers2):
    print(f"{a} + {b} = {a + b}")

print()

# 13. Practical examples

# Finding maximum value manually
numbers = [23, 45, 12, 67, 34, 89, 56]
max_num = numbers[0]
for num in numbers[1:]:
    if num > max_num:
        max_num = num
print(f"Maximum number: {max_num}")

# Counting occurrences
text = "hello world"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(f"Character count: {char_count}")

print()

# Processing a list of dictionaries
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 96}
]

print("Students with grade above 80:")
for student in students:
    if student["grade"] > 80:
        print(f"{student['name']}: {student['grade']}")

print()

# 14. Pattern printing with loops
print("Pattern printing:")

# Right triangle
print("Right triangle:")
for i in range(1, 6):
    print("*" * i)

print()

# Pyramid
print("Pyramid:")
for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

print()

# Number pattern
print("Number pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # New line after each row

print()

# 15. File processing simulation
print("Simulating file processing:")
file_data = [
    "user1,25,engineer",
    "user2,30,doctor",
    "user3,28,teacher",
    "user4,35,lawyer"
]

for line_num, line in enumerate(file_data, 1):
    parts = line.split(",")
    if len(parts) == 3:
        name, age, profession = parts
        print(f"Line {line_num}: {name} ({age}) - {profession}")
    else:
        print(f"Line {line_num}: Invalid format")

print()

# 16. Filtering and transforming data
print("Data filtering and transformation:")
temperatures_celsius = [0, 20, 25, 30, 35, 40]
print(f"Celsius temperatures: {temperatures_celsius}")

# Convert to Fahrenheit and filter
fahrenheit_above_80 = []
for temp_c in temperatures_celsius:
    temp_f = (temp_c * 9/5) + 32
    if temp_f > 80:
        fahrenheit_above_80.append(temp_f)

print(f"Fahrenheit temperatures above 80°F: {fahrenheit_above_80}")

print()

# 17. Nested data structures
print("Working with nested data:")
company = {
    "IT": [
        {"name": "Alice", "salary": 70000},
        {"name": "Bob", "salary": 75000}
    ],
    "HR": [
        {"name": "Charlie", "salary": 60000},
        {"name": "Diana", "salary": 65000}
    ]
}

for department, employees in company.items():
    print(f"\n{department} Department:")
    total_salary = 0
    for employee in employees:
        print(f"  {employee['name']}: ${employee['salary']:,}")
        total_salary += employee['salary']
    print(f"  Average salary: ${total_salary / len(employees):,.2f}")

print()

# 18. Performance considerations
print("Performance comparison:")

# Less efficient - repeated string concatenation
import time

start_time = time.time()
result = ""
for i in range(1000):
    result += str(i) + " "
slow_time = time.time() - start_time

# More efficient - using join
start_time = time.time()
numbers = []
for i in range(1000):
    numbers.append(str(i))
result = " ".join(numbers)
fast_time = time.time() - start_time

print(f"String concatenation time: {slow_time:.4f} seconds")
print(f"Join method time: {fast_time:.4f} seconds")

print()

# 19. Common loop patterns
print("Common loop patterns:")

# Accumulator pattern
total = 0
for i in range(1, 101):
    total += i
print(f"Sum of 1-100: {total}")

# Flag pattern
items = ["apple", "banana", "cherry"]
search_item = "banana"
found = False
for item in items:
    if item == search_item:
        found = True
        break
print(f"Found {search_item}: {found}")

# Counter pattern
text = "hello world hello"
word_count = 0
words = text.split()
for word in words:
    if word == "hello":
        word_count += 1
print(f"'hello' appears {word_count} times")

print()

# 20. Advanced techniques
print("Advanced for loop techniques:")

# Multiple assignment in for loop
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for number, letter in pairs:
    print(f"Number: {number}, Letter: {letter}")

print()

# Using * to unpack in for loop
data = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)]
for first, *middle, last in data:
    print(f"First: {first}, Middle: {middle}, Last: {last}")

print()

# Conditional assignment in loop
grades = [85, 92, 78, 96, 88]
letter_grades = []
for grade in grades:
    letter = 'A' if grade >= 90 else 'B' if grade >= 80 else 'C' if grade >= 70 else 'F'
    letter_grades.append(letter)
print(f"Numeric grades: {grades}")
print(f"Letter grades: {letter_grades}")
