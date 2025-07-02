## Understanding Functions
  This section will cover how to define and use functions in Python, including parameters, return values, and scope.

---

# What are Functions?

Functions are reusable pieces of code that perform a specific task. They help in organizing code and making it more modular.

---

# Defining a Function

To define a function in Python, use the `def` keyword followed by the function name and parentheses.

```python
def greet(name):
    return f"Hello, {name}!"
```

---

# Calling a Function

Once defined, you can call a function by using its name followed by parentheses.

```python
print(greet("Alice"))  # Output: Hello, Alice!
```

---

# Function Parameters

Functions can take parameters, which allow you to pass data into them.

```python
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8
```

---

# Return Values

Functions can return values using the `return` statement.

```python
def square(x):
    return x * x

result = square(4)
print(result)  # Output: 16
```

---

# Scope of Variables

Variables defined inside a function are local to that function and cannot be accessed outside of it.

```python
def my_function():
    local_var = "I'm local!"
    return local_var

print(my_function())  # Output: I'm local!
# print(local_var)  # This will raise an error
```

---

# Conclusion

Functions are a fundamental concept in Python that allow for code reuse and better organization. Understanding how to define and use functions is essential for effective programming.

---