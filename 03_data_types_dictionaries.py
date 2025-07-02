"""
Python Workshop - 03: Data Types - Dictionaries
===============================================

This file demonstrates Python dictionaries and their operations.
"""

# 1. Creating Dictionaries
empty_dict = {}
student = {"name": "Alice", "age": 25, "grade": "A"}
numbers_dict = {1: "one", 2: "two", 3: "three"}
mixed_dict = {"string_key": "value", 42: "number_key", True: "boolean_key"}

print("Empty dict:", empty_dict)
print("Student:", student)
print("Numbers dict:", numbers_dict)
print("Mixed dict:", mixed_dict)

# 2. Accessing Values
print(f"\nStudent name: {student['name']}")
print(f"Student age: {student['age']}")

# Using get() method (safer - returns None if key doesn't exist)
print(f"Student grade: {student.get('grade')}")
print(f"Student email: {student.get('email', 'Not provided')}")  # Default value

# 3. Adding and Updating Values
student["email"] = "alice@example.com"  # Add new key-value pair
student["age"] = 26  # Update existing value
student.update({"city": "New York", "major": "Computer Science"})  # Update multiple

print(f"\nUpdated student: {student}")

# 4. Removing Elements
# Using del
temp_dict = student.copy()
del temp_dict["major"]
print(f"After del: {temp_dict}")

# Using pop() - removes and returns the value
temp_dict = student.copy()
removed_email = temp_dict.pop("email")
print(f"Removed email: {removed_email}")
print(f"After pop: {temp_dict}")

# Using popitem() - removes and returns the last key-value pair
temp_dict = student.copy()
last_item = temp_dict.popitem()
print(f"Last item removed: {last_item}")
print(f"After popitem: {temp_dict}")

# 5. Dictionary Methods
print(f"\nOriginal student: {student}")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# 6. Checking Membership
print(f"\n'name' in student: {'name' in student}")
print(f"'phone' in student: {'phone' in student}")
print(f"'Alice' in student.values(): {'Alice' in student.values()}")

# 7. Dictionary Comprehensions
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"\nSquares dict: {squares_dict}")

# Filter dictionary
high_scores = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 78}
passed_students = {name: score for name, score in high_scores.items() if score >= 90}
print(f"High scores: {high_scores}")
print(f"Students with 90+: {passed_students}")

# 8. Nested Dictionaries
company = {
    "employees": {
        "john": {"department": "IT", "salary": 50000},
        "jane": {"department": "HR", "salary": 55000},
        "bob": {"department": "IT", "salary": 52000}
    },
    "departments": {
        "IT": {"budget": 200000, "head": "john"},
        "HR": {"budget": 150000, "head": "jane"}
    }
}

print(f"\nCompany structure: {company}")
print(f"John's salary: {company['employees']['john']['salary']}")
print(f"IT department head: {company['departments']['IT']['head']}")

# 9. Dictionary Operations
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"b": 20, "e": 5}  # Note: 'b' exists in dict1

# Merging dictionaries (Python 3.9+)
# merged = dict1 | dict2
# For older Python versions:
merged = {**dict1, **dict2}
print(f"\nDict1: {dict1}")
print(f"Dict2: {dict2}")
print(f"Merged: {merged}")

# Update with another dictionary
dict1_copy = dict1.copy()
dict1_copy.update(dict3)  # 'b' will be overwritten
print(f"Dict1 updated with dict3: {dict1_copy}")

# 10. Common Patterns and Use Cases

# Counting items
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"\nCharacter count: {char_count}")

# Using dictionary as a lookup table
grade_to_gpa = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
student_grades = ["A", "B", "A", "C", "B"]
gpa_values = [grade_to_gpa[grade] for grade in student_grades]
average_gpa = sum(gpa_values) / len(gpa_values)
print(f"Grades: {student_grades}")
print(f"Average GPA: {average_gpa:.2f}")

# Grouping data
students_data = [
    {"name": "Alice", "department": "CS"},
    {"name": "Bob", "department": "Math"},
    {"name": "Charlie", "department": "CS"},
    {"name": "Diana", "department": "Physics"},
    {"name": "Eve", "department": "Math"}
]

by_department = {}
for student in students_data:
    dept = student["department"]
    if dept not in by_department:
        by_department[dept] = []
    by_department[dept].append(student["name"])

print(f"\nStudents by department: {by_department}")

# 11. Dictionary vs List comparison
print(f"\nDictionary characteristics:")
print("- Unordered (before Python 3.7) / Insertion ordered (Python 3.7+)")
print("- Key-value pairs")
print("- Keys must be immutable (strings, numbers, tuples)")
print("- Fast lookup by key O(1)")
print("- Mutable")

# Performance example
import time

# Dictionary lookup
large_dict = {i: f"value_{i}" for i in range(100000)}
start = time.time()
result = large_dict.get(99999)
dict_time = time.time() - start

# List search
large_list = [(i, f"value_{i}") for i in range(100000)]
start = time.time()
result = next((value for key, value in large_list if key == 99999), None)
list_time = time.time() - start

print(f"\nDictionary lookup time: {dict_time:.6f} seconds")
print(f"List search time: {list_time:.6f} seconds")
