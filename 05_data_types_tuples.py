"""
Python Workshop - 05: Data Types - Tuples
=========================================

This file demonstrates Python tuples and their operations.
"""

# 1. Creating Tuples
empty_tuple = ()
single_element = (42,)  # Note the comma - without it, it's just parentheses
coordinates = (10, 20)
rgb_color = (255, 128, 0)
mixed_tuple = (1, "hello", 3.14, True)

print("Empty tuple:", empty_tuple)
print("Single element:", single_element)
print("Coordinates:", coordinates)
print("RGB color:", rgb_color)
print("Mixed tuple:", mixed_tuple)

# Creating tuples without parentheses (tuple packing)
point = 5, 10  # Parentheses are optional
name_age = "Alice", 25
print(f"\nPoint: {point}")
print(f"Name and age: {name_age}")

# Creating from other iterables
list_to_tuple = tuple([1, 2, 3, 4])
string_to_tuple = tuple("hello")
print(f"List to tuple: {list_to_tuple}")
print(f"String to tuple: {string_to_tuple}")

# 2. Accessing Elements (same as lists)
fruits = ("apple", "banana", "cherry", "date")
print(f"\nFirst fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second fruit: {fruits[1]}")

# 3. Slicing (same as lists)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"\nNumbers: {numbers}")
print(f"First 3: {numbers[:3]}")
print(f"Last 3: {numbers[-3:]}")
print(f"Every second: {numbers[::2]}")
print(f"Reversed: {numbers[::-1]}")

# 4. Tuple Immutability
original_tuple = (1, 2, 3)
print(f"\nOriginal tuple: {original_tuple}")

# This would cause an error:
# original_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# But you can create a new tuple
new_tuple = original_tuple + (4, 5)
print(f"New tuple (concatenated): {new_tuple}")

# 5. Tuple Methods (limited compared to lists)
sample_tuple = (1, 2, 3, 2, 4, 2, 5)
print(f"\nSample tuple: {sample_tuple}")
print(f"Count of 2: {sample_tuple.count(2)}")
print(f"Index of first 3: {sample_tuple.index(3)}")

# 6. Tuple Unpacking
coordinates = (10, 20)
x, y = coordinates  # Tuple unpacking
print(f"\nCoordinates: {coordinates}")
print(f"x = {x}, y = {y}")

# Multiple assignment using unpacking
person = ("Alice", 25, "Engineer")
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Swapping variables using tuples
a = 5
b = 10
print(f"\nBefore swap: a = {a}, b = {b}")
a, b = b, a  # Elegant way to swap
print(f"After swap: a = {a}, b = {b}")

# Extended unpacking (Python 3+)
numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
print(f"\nNumbers: {numbers}")
print(f"First: {first}, Middle: {middle}, Last: {last}")

first, second, *rest = numbers
print(f"First: {first}, Second: {second}, Rest: {rest}")

# 7. Nested Tuples
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"\nMatrix: {matrix}")
print(f"Element at [1][2]: {matrix[1][2]}")

# Tuple of tuples for coordinates
points = ((0, 0), (1, 1), (2, 4), (3, 9))
print(f"Points: {points}")

# 8. Tuple Operations
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(f"\nTuple1: {tuple1}")
print(f"Tuple2: {tuple2}")
print(f"Combined: {combined}")

# Repetition
repeated = tuple1 * 3
print(f"Repeated: {repeated}")

# Membership testing
print(f"2 in tuple1: {2 in tuple1}")
print(f"7 in tuple1: {7 in tuple1}")

# Length
print(f"Length of tuple1: {len(tuple1)}")

# 9. Comparison
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 4)
tuple_c = (1, 2, 3)

print(f"\nTuple A: {tuple_a}")
print(f"Tuple B: {tuple_b}")
print(f"Tuple C: {tuple_c}")
print(f"A == B: {tuple_a == tuple_b}")
print(f"A == C: {tuple_a == tuple_c}")
print(f"A < B: {tuple_a < tuple_b}")  # Lexicographic comparison

# 10. Practical Uses of Tuples

# Function returning multiple values
def get_name_age():
    return "Bob", 30

result = get_name_age()
print(f"\nFunction result: {result}")
name, age = get_name_age()  # Unpacking
print(f"Unpacked: {name}, {age}")

# Dictionary with tuple keys
locations = {
    (0, 0): "Origin",
    (1, 1): "Northeast",
    (-1, -1): "Southwest",
    (0, 1): "North"
}
print(f"\nLocations: {locations}")
print(f"Location at (0,0): {locations[(0, 0)]}")

# Configuration settings (immutable)
DATABASE_CONFIG = ("localhost", 5432, "mydb", "user")
host, port, database, username = DATABASE_CONFIG
print(f"\nDB Config: Host={host}, Port={port}, DB={database}, User={username}")

# 11. Named Tuples (from collections module)
from collections import namedtuple

# Define a named tuple
Point = namedtuple('Point', ['x', 'y'])
Color = namedtuple('Color', ['red', 'green', 'blue'])

# Create instances
p1 = Point(10, 20)
p2 = Point(x=30, y=40)  # Can use keyword arguments
color = Color(255, 128, 0)

print(f"\nNamed tuples:")
print(f"Point 1: {p1}")
print(f"Point 1 x: {p1.x}, y: {p1.y}")
print(f"Point 2: {p2}")
print(f"Color: {color}")
print(f"Red component: {color.red}")

# Named tuples are still tuples
print(f"Point 1 as tuple: {tuple(p1)}")
print(f"Point 1[0]: {p1[0]}")

# 12. When to Use Tuples vs Lists
print(f"\nTuples vs Lists:")
print("Use Tuples when:")
print("- Data should not change (immutable)")
print("- You need to use data as dictionary keys")
print("- Returning multiple values from functions")
print("- Coordinates, RGB values, database records")
print("- Configuration settings")

print("\nUse Lists when:")
print("- Data needs to change (mutable)")
print("- You need to add/remove elements")
print("- Order matters and you need to sort")
print("- Working with collections that grow/shrink")

# 13. Performance Comparison
import time

# Tuple creation vs List creation
start = time.time()
for i in range(100000):
    t = (1, 2, 3, 4, 5)
tuple_time = time.time() - start

start = time.time()
for i in range(100000):
    l = [1, 2, 3, 4, 5]
list_time = time.time() - start

print(f"\nPerformance (100k creations):")
print(f"Tuple creation time: {tuple_time:.4f} seconds")
print(f"List creation time: {list_time:.4f} seconds")

# Memory usage comparison
import sys
sample_tuple = (1, 2, 3, 4, 5)
sample_list = [1, 2, 3, 4, 5]

print(f"\nMemory usage:")
print(f"Tuple size: {sys.getsizeof(sample_tuple)} bytes")
print(f"List size: {sys.getsizeof(sample_list)} bytes")
