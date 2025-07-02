"""
Python Workshop - 04: Data Types - Sets
=======================================

This file demonstrates Python sets and their operations.
"""

# 1. Creating Sets
empty_set = set()  # Note: {} creates an empty dictionary, not set
numbers_set = {1, 2, 3, 4, 5}
fruits_set = {"apple", "banana", "cherry"}
mixed_set = {1, "hello", 3.14, True}

print("Empty set:", empty_set)
print("Numbers set:", numbers_set)
print("Fruits set:", fruits_set)
print("Mixed set:", mixed_set)

# Creating set from other iterables
list_to_set = set([1, 2, 3, 2, 1])  # Duplicates removed
string_to_set = set("hello")  # Each character becomes an element
print(f"\nList to set: {list_to_set}")
print(f"String to set: {string_to_set}")

# 2. Set Properties
duplicate_numbers = {1, 2, 3, 2, 1, 4, 3}
print(f"\nSet with duplicates: {duplicate_numbers}")  # Duplicates automatically removed
print(f"Set is unordered and contains unique elements only")

# 3. Adding Elements
fruits_copy = fruits_set.copy()
fruits_copy.add("date")
print(f"\nAfter add: {fruits_copy}")

fruits_copy.update(["elderberry", "fig", "grape"])  # Add multiple elements
print(f"After update: {fruits_copy}")

# Adding duplicate (no effect)
fruits_copy.add("apple")  # apple already exists
print(f"After adding duplicate: {fruits_copy}")

# 4. Removing Elements
fruits_copy = {"apple", "banana", "cherry", "date"}

# Using remove() - raises KeyError if element doesn't exist
fruits_copy.remove("banana")
print(f"\nAfter remove: {fruits_copy}")

# Using discard() - doesn't raise error if element doesn't exist
fruits_copy.discard("elderberry")  # Doesn't exist, but no error
fruits_copy.discard("cherry")      # Exists, gets removed
print(f"After discard: {fruits_copy}")

# Using pop() - removes and returns arbitrary element
fruits_copy = {"apple", "banana", "cherry", "date"}
popped = fruits_copy.pop()
print(f"Popped element: {popped}")
print(f"After pop: {fruits_copy}")

# Using clear() - removes all elements
temp_set = {1, 2, 3}
temp_set.clear()
print(f"After clear: {temp_set}")

# 5. Set Operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {1, 2, 3}

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")
print(f"Set C: {set_c}")

# Union (elements in either set)
union1 = set_a | set_b
union2 = set_a.union(set_b)
print(f"Union A|B: {union1}")
print(f"Union A.union(B): {union2}")

# Intersection (elements in both sets)
intersection1 = set_a & set_b
intersection2 = set_a.intersection(set_b)
print(f"Intersection A&B: {intersection1}")
print(f"Intersection A.intersection(B): {intersection2}")

# Difference (elements in first set but not in second)
difference1 = set_a - set_b
difference2 = set_a.difference(set_b)
print(f"Difference A-B: {difference1}")
print(f"Difference B-A: {set_b - set_a}")

# Symmetric Difference (elements in either set, but not in both)
sym_diff1 = set_a ^ set_b
sym_diff2 = set_a.symmetric_difference(set_b)
print(f"Symmetric Difference A^B: {sym_diff1}")

# 6. Set Relationships
print(f"\nSet relationships:")
print(f"Is C subset of A? {set_c.issubset(set_a)}")
print(f"Is A superset of C? {set_a.issuperset(set_c)}")
print(f"Are A and B disjoint? {set_a.isdisjoint(set_b)}")

set_d = {10, 11, 12}
print(f"Are A and D disjoint? {set_a.isdisjoint(set_d)}")

# 7. Membership Testing
print(f"\nMembership testing:")
print(f"3 in set_a: {3 in set_a}")
print(f"9 in set_a: {9 in set_a}")
print(f"6 not in set_a: {6 not in set_a}")

# 8. Set Comprehensions
squares_set = {x**2 for x in range(1, 6)}
print(f"\nSquares set: {squares_set}")

even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Set comprehension with string
vowels = {char.lower() for char in "Hello World" if char.lower() in 'aeiou'}
print(f"Vowels in 'Hello World': {vowels}")

# 9. Practical Examples

# Remove duplicates from a list
numbers_with_duplicates = [1, 2, 3, 2, 4, 1, 5, 3]
unique_numbers = list(set(numbers_with_duplicates))
print(f"\nOriginal list: {numbers_with_duplicates}")
print(f"Unique numbers: {unique_numbers}")

# Find common elements between lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"Common elements: {common}")

# Find unique words in text
text = "the quick brown fox jumps over the lazy dog the fox is quick"
words = text.split()
unique_words = set(words)
print(f"Text: {text}")
print(f"Unique words: {unique_words}")
print(f"Number of unique words: {len(unique_words)}")

# 10. Set vs List vs Dictionary comparison
print(f"\nData structure comparison:")
print("Sets:")
print("- Unordered collection")
print("- No duplicate elements")
print("- Mutable")
print("- Fast membership testing O(1)")
print("- Mathematical set operations")
print("- Elements must be immutable (hashable)")

# Performance comparison
import time

# Set membership test
large_set = set(range(100000))
start = time.time()
result = 99999 in large_set
set_time = time.time() - start

# List membership test
large_list = list(range(100000))
start = time.time()
result = 99999 in large_list
list_time = time.time() - start

print(f"\nSet membership test time: {set_time:.6f} seconds")
print(f"List membership test time: {list_time:.6f} seconds")

# 11. Frozen Sets (Immutable sets)
regular_set = {1, 2, 3}
frozen_set_example = frozenset([1, 2, 3, 4])

print(f"\nRegular set: {regular_set}")
print(f"Frozen set: {frozen_set_example}")

# Frozen sets can be dictionary keys or elements of sets
dict_with_frozenset_key = {frozen_set_example: "This works!"}
set_with_frozenset = {frozenset([1, 2]), frozenset([3, 4])}

print(f"Dict with frozenset key: {dict_with_frozenset_key}")
print(f"Set with frozensets: {set_with_frozenset}")

# This would cause an error:
# dict_with_set_key = {regular_set: "This doesn't work!"}  # TypeError
