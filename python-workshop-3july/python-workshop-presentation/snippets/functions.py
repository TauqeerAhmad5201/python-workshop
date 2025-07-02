def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_even(num):
    return num % 2 == 0

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq