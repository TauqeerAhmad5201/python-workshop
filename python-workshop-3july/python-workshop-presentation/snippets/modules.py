# This file contains examples of creating and using modules in Python, illustrating how to organize code effectively.

# Example of a simple module
def greet(name):
    return f"Hello, {name}!"

# Example of a module with multiple functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Example of using a module
if __name__ == "__main__":
    print(greet("World"))
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(10, 4))