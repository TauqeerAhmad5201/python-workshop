"""
Python Workshop - 02: Data Types - Lists
=========================================

This file demonstrates Python lists and their operations.
"""

# 1. Creating Lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry", "date"]
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]

print("Empty list:", empty_list)
print("Numbers:", numbers)
print("Fruits:", fruits)
print("Mixed list:", mixed_list)

# 2. Accessing Elements (Indexing)
print(f"\nFirst fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second number: {numbers[1]}")

# 3. Slicing
print(f"\nFirst 3 numbers: {numbers[:3]}")
print(f"Last 2 fruits: {fruits[-2:]}")
print(f"Every second fruit: {fruits[::2]}")
print(f"Reversed fruits: {fruits[::-1]}")

# 4. List Methods
# Adding elements
fruits.append("elderberry")  # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "apricot")  # Insert at index
print(f"After insert: {fruits}")

fruits.extend(["fig", "grape"])  # Add multiple elements
print(f"After extend: {fruits}")

# Removing elements
removed_fruit = fruits.pop()  # Remove and return last element
print(f"Removed: {removed_fruit}, List: {fruits}")

fruits.remove("apricot")  # Remove first occurrence
print(f"After remove: {fruits}")

# Other useful methods
numbers_copy = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nOriginal: {numbers_copy}")
print(f"Count of 1: {numbers_copy.count(1)}")
print(f"Index of 4: {numbers_copy.index(4)}")

numbers_copy.sort()  # Sort in place
print(f"Sorted: {numbers_copy}")

numbers_copy.reverse()  # Reverse in place
print(f"Reversed: {numbers_copy}")

# 5. List Comprehensions
squares = [x**2 for x in range(1, 6)]
print(f"\nSquares: {squares}")

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

fruit_lengths = [len(fruit) for fruit in fruits]
print(f"Fruit lengths: {fruit_lengths}")

# 6. Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nMatrix: {matrix}")
print(f"Element at [1][2]: {matrix[1][2]}")

# 7. Common Operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"\nCombined: {combined}")

# Repetition
repeated = list1 * 3
print(f"Repeated: {repeated}")

# Membership testing
print(f"2 in list1: {2 in list1}")
print(f"7 in list1: {7 in list1}")

# Length
print(f"Length of fruits: {len(fruits)}")

# 8. Useful Functions with Lists
numbers_for_functions = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nNumbers: {numbers_for_functions}")
print(f"Sum: {sum(numbers_for_functions)}")
print(f"Max: {max(numbers_for_functions)}")
print(f"Min: {min(numbers_for_functions)}")
print(f"Sorted (new list): {sorted(numbers_for_functions)}")
print(f"Reversed (new list): {list(reversed(numbers_for_functions))}")

# 9. Converting between types
string_numbers = "12345"
digit_list = list(string_numbers)
print(f"\nString to list: {digit_list}")

number_list = [1, 2, 3, 4, 5]
joined_string = ''.join(map(str, number_list))
print(f"List to string: {joined_string}")

# 10. List vs String comparison
text = "hello"
text_list = list(text)
print(f"\nString: {text}")
print(f"As list: {text_list}")
print(f"Back to string: {''.join(text_list)}")
