"""
Python Workshop - 08: Control Flow - While Loops
================================================

This file demonstrates Python while loops and their various uses.
"""

# 1. Basic while loop
print("Basic while loop:")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1  # Don't forget to increment!

print()

# 2. While loop with user input simulation
print("While loop with condition:")
number = 1
while number <= 10:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    number += 1

print()

# 3. While loop with break
print("While loop with break:")
i = 0
while True:  # Infinite loop
    if i >= 5:
        print("Breaking out of loop")
        break
    print(f"Iteration: {i}")
    i += 1

print()

# 4. While loop with continue
print("While loop with continue:")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:  # Skip even numbers
        continue
    print(f"Odd number: {num}")

print()

# 5. While-else construct
print("While-else (else executes if loop completes normally):")
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1
else:
    print("Loop completed successfully")

print()

print("While-else with break (else doesn't execute):")
counter = 0
while counter < 10:
    if counter == 3:
        print("Breaking early")
        break
    print(f"Counter: {counter}")
    counter += 1
else:
    print("This won't be printed because of break")

print()

# 6. Nested while loops
print("Nested while loops - Multiplication table:")
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        product = i * j
        print(f"{i} x {j} = {product}")
        j += 1
    print()  # Empty line after each row
    i += 1

# 7. Input validation with while loop
def get_valid_age():
    """Simulate getting valid input from user"""
    # In real scenario, you'd use input()
    test_inputs = ["-5", "abc", "150", "25"]  # Simulating user inputs
    input_index = 0
    
    while input_index < len(test_inputs):
        user_input = test_inputs[input_index]
        print(f"Simulating input: '{user_input}'")
        
        try:
            age = int(user_input)
            if 0 <= age <= 120:
                print(f"Valid age: {age}")
                return age
            else:
                print("Age must be between 0 and 120")
        except ValueError:
            print("Please enter a valid number")
        
        input_index += 1
    
    print("No more test inputs available")
    return None

print("Input validation example:")
valid_age = get_valid_age()
print()

# 8. Search algorithms with while
print("Linear search with while loop:")
numbers = [12, 45, 23, 67, 34, 89, 56, 78]
target = 67
index = 0
found = False

while index < len(numbers) and not found:
    if numbers[index] == target:
        found = True
        print(f"Found {target} at index {index}")
    else:
        index += 1

if not found:
    print(f"{target} not found in the list")

print()

# 9. Accumulator pattern with while
print("Sum calculation with while loop:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
index = 0

while index < len(numbers):
    total += numbers[index]
    index += 1

print(f"Sum of {numbers}: {total}")

print()

# 10. Factorial calculation
print("Factorial calculation:")
def factorial_while(n):
    if n < 0:
        return None
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

test_numbers = [0, 1, 5, 7]
for num in test_numbers:
    fact = factorial_while(num)
    print(f"{num}! = {fact}")

print()

# 11. String processing with while
print("String processing with while:")
text = "Hello, World!"
index = 0
vowels = "aeiouAEIOU"
vowel_count = 0

while index < len(text):
    if text[index] in vowels:
        vowel_count += 1
        print(f"Found vowel '{text[index]}' at position {index}")
    index += 1

print(f"Total vowels found: {vowel_count}")

print()

# 12. Menu system simulation
def show_menu():
    print("\n--- Menu ---")
    print("1. View balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def bank_system_simulation():
    balance = 1000.0
    # Simulating user choices
    user_choices = ["1", "2", "100", "3", "50", "1", "4"]
    choice_index = 0
    
    print("Bank System Simulation:")
    
    while choice_index < len(user_choices):
        show_menu()
        choice = user_choices[choice_index]
        print(f"User chose: {choice}")
        choice_index += 1
        
        if choice == "1":
            print(f"Your balance: ${balance:.2f}")
        
        elif choice == "2":
            if choice_index < len(user_choices):
                amount_str = user_choices[choice_index]
                choice_index += 1
                try:
                    amount = float(amount_str)
                    if amount > 0:
                        balance += amount
                        print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
                    else:
                        print("Amount must be positive")
                except ValueError:
                    print("Invalid amount")
        
        elif choice == "3":
            if choice_index < len(user_choices):
                amount_str = user_choices[choice_index]
                choice_index += 1
                try:
                    amount = float(amount_str)
                    if amount > 0:
                        if amount <= balance:
                            balance -= amount
                            print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")
                        else:
                            print("Insufficient funds")
                    else:
                        print("Amount must be positive")
                except ValueError:
                    print("Invalid amount")
        
        elif choice == "4":
            print("Thank you for using our bank system!")
            break
        
        else:
            print("Invalid choice. Please try again.")
        
        print()

bank_system_simulation()

# 13. Game simulation - Guessing game
print("Number guessing game simulation:")
import random

def guessing_game():
    secret_number = random.randint(1, 10)
    # Simulating guesses
    guesses = [3, 7, 5, 6]  # Predetermined guesses for demonstration
    guess_count = 0
    max_attempts = 4
    
    print(f"Guess the number between 1 and 10! (Secret: {secret_number})")
    
    while guess_count < max_attempts and guess_count < len(guesses):
        guess = guesses[guess_count]
        guess_count += 1
        
        print(f"Attempt {guess_count}: Guessing {guess}")
        
        if guess == secret_number:
            print(f"Congratulations! You found it in {guess_count} attempts!")
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
    
    print(f"Game over! The number was {secret_number}")

guessing_game()
print()

# 14. Data processing with while
print("Processing data until condition met:")
sensor_readings = [20, 22, 25, 30, 35, 42, 45, 50, 55, 38, 30, 25]
reading_index = 0
max_safe_temp = 40
alarm_triggered = False

print("Monitoring temperature readings:")
while reading_index < len(sensor_readings) and not alarm_triggered:
    current_temp = sensor_readings[reading_index]
    print(f"Reading {reading_index + 1}: {current_temp}°C", end="")
    
    if current_temp > max_safe_temp:
        print(" - ALARM! Temperature too high!")
        alarm_triggered = True
    else:
        print(" - Normal")
    
    reading_index += 1

if alarm_triggered:
    print("System shutdown due to high temperature")
else:
    print("All readings normal")

print()

# 15. Queue simulation
print("Queue processing simulation:")
queue = ["Task1", "Task2", "Task3", "Task4", "Task5"]
processing_time = 0

print("Processing queue:")
while queue:  # While queue is not empty
    current_task = queue.pop(0)  # Remove first item
    processing_time += 1
    print(f"Time {processing_time}: Processing {current_task}")
    
    # Simulate new tasks arriving
    if processing_time == 2:
        queue.append("UrgentTask")
        print("  -> New urgent task added to queue")
    
    print(f"  -> Remaining tasks: {queue}")

print("All tasks completed!")

print()

# 16. Iterative improvement
print("Iterative improvement - Square root approximation:")
def sqrt_approximation(number, tolerance=0.001):
    if number < 0:
        return None
    
    guess = number / 2.0  # Initial guess
    iteration = 0
    
    print(f"Finding square root of {number}:")
    
    while True:
        iteration += 1
        better_guess = (guess + number / guess) / 2.0
        difference = abs(guess - better_guess)
        
        print(f"Iteration {iteration}: {better_guess:.6f} (diff: {difference:.6f})")
        
        if difference < tolerance:
            break
        
        guess = better_guess
    
    return better_guess

result = sqrt_approximation(25)
print(f"Final result: {result:.6f} (actual: {25**0.5:.6f})")

print()

# 17. State machine simulation
print("State machine simulation - Traffic light:")
def traffic_light_simulation():
    states = ["RED", "GREEN", "YELLOW"]
    current_state = 0
    time_in_state = 0
    state_durations = [3, 5, 2]  # RED: 3s, GREEN: 5s, YELLOW: 2s
    total_time = 0
    max_time = 20
    
    print("Traffic light simulation:")
    
    while total_time < max_time:
        current_light = states[current_state]
        duration = state_durations[current_state]
        
        print(f"Time {total_time}: {current_light} (remaining: {duration - time_in_state}s)")
        
        time_in_state += 1
        total_time += 1
        
        if time_in_state >= duration:
            time_in_state = 0
            current_state = (current_state + 1) % len(states)
    
    print("Simulation ended")

traffic_light_simulation()

print()

# 18. While vs For comparison
print("When to use while vs for:")
print("Use WHILE when:")
print("- You don't know how many iterations you need")
print("- The loop depends on a condition that might change unpredictably")
print("- You're waiting for user input or external events")
print("- Implementing algorithms that converge to a solution")

print("\nUse FOR when:")
print("- You know the number of iterations")
print("- You're iterating over a collection")
print("- You need the index along with the value")
print("- The iteration pattern is predictable")

print()

# 19. Common pitfalls and best practices
print("Common while loop pitfalls:")

# Infinite loop example (commented out)
# print("DANGER: Infinite loop (commented out)")
# while True:
#     print("This would run forever!")

# Forgetting to update loop variable
print("Example of properly updating loop variable:")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1  # IMPORTANT: Don't forget this!

print()

# Off-by-one errors
print("Avoiding off-by-one errors:")
# Wrong way
print("Inclusive range (0 to 5):")
i = 0
while i <= 5:  # Note: <= for inclusive
    print(i, end=" ")
    i += 1
print()

# Right way for exclusive range
print("Exclusive range (0 to 4):")
i = 0
while i < 5:  # Note: < for exclusive
    print(i, end=" ")
    i += 1
print()

print()

# 20. Performance considerations
print("Performance considerations:")
import time

# Inefficient: checking length repeatedly
def inefficient_while():
    data = list(range(10000))
    result = []
    index = 0
    
    start = time.time()
    while index < len(data):  # len() called every iteration
        result.append(data[index] * 2)
        index += 1
    end = time.time()
    
    return end - start

# Efficient: cache the length
def efficient_while():
    data = list(range(10000))
    result = []
    index = 0
    length = len(data)  # Calculate once
    
    start = time.time()
    while index < length:
        result.append(data[index] * 2)
        index += 1
    end = time.time()
    
    return end - start

slow_time = inefficient_while()
fast_time = efficient_while()

print(f"Inefficient while loop: {slow_time:.4f} seconds")
print(f"Efficient while loop: {fast_time:.4f} seconds")
print(f"Improvement: {slow_time/fast_time:.2f}x faster")
