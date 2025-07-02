"""
Python Workshop - 09: Exception Handling - Try-Except
=====================================================

This file demonstrates Python exception handling with try-except blocks.
"""

# 1. Basic try-except
print("1. Basic try-except:")
try:
    result = 10 / 0  # This will raise ZeroDivisionError
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

print()

# 2. Handling different types of exceptions
print("2. Multiple exception types:")

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid data types for division")
        return None

# Test cases
test_cases = [(10, 2), (10, 0), (10, "2"), ("10", 2)]
for a, b in test_cases:
    print(f"safe_divide({a}, {b}) =", safe_divide(a, b))

print()

# 3. Catching multiple exceptions in one block
print("3. Catching multiple exceptions:")

def process_data(data):
    try:
        # Convert to integer
        number = int(data)
        # Perform calculation
        result = 100 / number
        # Access list element
        values = [1, 2, 3]
        element = values[number]
        return f"Success: {result}, Element: {element}"
    
    except (ValueError, TypeError):
        return "Error: Invalid input data"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except IndexError:
        return "Error: Index out of range"

# Test different scenarios
test_inputs = ["5", "0", "abc", "10", None]
for data in test_inputs:
    result = process_data(data)
    print(f"process_data({data!r}) -> {result}")

print()

# 4. Using else clause
print("4. Try-except-else:")

def file_operation_simulation(filename):
    try:
        # Simulate file operations
        if filename == "nonexistent.txt":
            raise FileNotFoundError("File not found")
        elif filename == "corrupted.txt":
            raise ValueError("File is corrupted")
        else:
            print(f"Successfully opened {filename}")
            return f"Content of {filename}"
    
    except FileNotFoundError as e:
        print(f"File error: {e}")
        return None
    except ValueError as e:
        print(f"Data error: {e}")
        return None
    else:
        # This runs only if no exception occurred
        print("File operation completed successfully")
        return "File processed"

# Test the function
test_files = ["data.txt", "nonexistent.txt", "corrupted.txt"]
for filename in test_files:
    print(f"\nTrying to open {filename}:")
    result = file_operation_simulation(filename)
    print(f"Result: {result}")

print()

# 5. Using finally clause
print("5. Try-except-finally:")

def database_operation_simulation(operation):
    print(f"Connecting to database...")
    
    try:
        if operation == "read":
            print("Reading data from database")
            return "Data retrieved"
        elif operation == "write":
            print("Writing data to database")
            raise PermissionError("Write permission denied")
        else:
            raise ValueError("Invalid operation")
    
    except PermissionError as e:
        print(f"Permission error: {e}")
        return None
    except ValueError as e:
        print(f"Value error: {e}")
        return None
    else:
        print("Database operation successful")
    finally:
        # This always runs, regardless of exceptions
        print("Closing database connection")

# Test the function
operations = ["read", "write", "delete"]
for op in operations:
    print(f"\n--- Operation: {op} ---")
    result = database_operation_simulation(op)
    print(f"Final result: {result}")

print()

# 6. Raising custom exceptions
print("6. Raising custom exceptions:")

class InvalidAgeError(Exception):
    """Custom exception for invalid age values"""
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient funds: Balance ${balance}, Requested ${amount}"
        super().__init__(self.message)

def create_user_account(name, age, initial_balance):
    try:
        # Validate age
        if not isinstance(age, int) or age < 0 or age > 120:
            raise InvalidAgeError(age)
        
        # Validate balance
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        print(f"Account created for {name}, age {age}, balance ${initial_balance}")
        return {"name": name, "age": age, "balance": initial_balance}
    
    except InvalidAgeError as e:
        print(f"Age validation error: {e}")
        return None
    except ValueError as e:
        print(f"Value error: {e}")
        return None

# Test account creation
test_accounts = [
    ("Alice", 25, 1000),
    ("Bob", -5, 500),
    ("Charlie", 150, 2000),
    ("Diana", 30, -100)
]

for name, age, balance in test_accounts:
    print(f"\nCreating account for {name}:")
    account = create_user_account(name, age, balance)

print()

# 7. Exception chaining
print("7. Exception chaining:")

def process_user_data(user_data):
    try:
        # First, validate the data structure
        if not isinstance(user_data, dict):
            raise TypeError("User data must be a dictionary")
        
        # Then process specific fields
        try:
            email = user_data["email"]
            if "@" not in email:
                raise ValueError("Invalid email format")
        except KeyError:
            raise ValueError("Email field is required") from None
        
        try:
            age = int(user_data["age"])
        except (KeyError, ValueError) as e:
            raise ValueError("Valid age is required") from e
        
        return f"User processed: {email}, age {age}"
    
    except (TypeError, ValueError) as e:
        print(f"Processing error: {e}")
        return None

# Test with various data
test_data = [
    {"email": "user@example.com", "age": "25"},
    {"email": "invalid-email", "age": "30"},
    {"age": "25"},  # Missing email
    {"email": "user@example.com", "age": "invalid"},
    "not a dictionary"
]

for i, data in enumerate(test_data, 1):
    print(f"\nTest {i}: {data}")
    result = process_user_data(data)

print()

# 8. Context managers with exception handling
print("8. Context managers and exceptions:")

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
    
    def __enter__(self):
        print(f"Connecting to {self.db_name}")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Disconnecting from {self.db_name}")
        self.connected = False
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
        return False  # Don't suppress exceptions
    
    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Not connected to database")
        
        if "DROP" in sql.upper():
            raise PermissionError("DROP operations not allowed")
        
        return f"Query result for: {sql}"

# Using context manager with exception handling
def database_operation(sql_query):
    try:
        with DatabaseConnection("mydb") as db:
            result = db.query(sql_query)
            print(f"Success: {result}")
            return result
    except PermissionError as e:
        print(f"Permission denied: {e}")
        return None
    except RuntimeError as e:
        print(f"Runtime error: {e}")
        return None

# Test database operations
queries = [
    "SELECT * FROM users",
    "DROP TABLE users",
    "INSERT INTO users VALUES (1, 'Alice')"
]

for query in queries:
    print(f"\n--- Executing: {query} ---")
    result = database_operation(query)

print()

# 9. Exception handling in loops
print("9. Exception handling in loops:")

def process_number_list(numbers):
    results = []
    errors = []
    
    for i, num in enumerate(numbers):
        try:
            # Try to convert to float and calculate square root
            value = float(num)
            if value < 0:
                raise ValueError("Cannot calculate square root of negative number")
            
            sqrt_value = value ** 0.5
            results.append((i, num, sqrt_value))
            print(f"✓ {num} -> {sqrt_value:.2f}")
        
        except ValueError as e:
            error_msg = f"Error with '{num}': {e}"
            errors.append((i, num, str(e)))
            print(f"✗ {error_msg}")
        except Exception as e:
            error_msg = f"Unexpected error with '{num}': {e}"
            errors.append((i, num, str(e)))
            print(f"✗ {error_msg}")
    
    return results, errors

# Test with mixed data
test_numbers = ["4", "9", "-1", "abc", "16", "", "25.5", None]
print("Processing number list:")
results, errors = process_number_list(test_numbers)

print(f"\nSuccessful calculations: {len(results)}")
print(f"Errors encountered: {len(errors)}")

print()

# 10. Nested exception handling
print("10. Nested exception handling:")

def complex_data_processing(data):
    """Demonstrates nested try-except blocks"""
    try:
        print(f"Processing data: {data}")
        
        # Outer validation
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary")
        
        results = {}
        
        # Process each field with individual error handling
        for key, value in data.items():
            try:
                if key == "numbers":
                    try:
                        # Convert strings to numbers and sum them
                        numbers = [float(x) for x in value]
                        results[key] = sum(numbers)
                    except ValueError as e:
                        raise ValueError(f"Invalid number in {key}: {e}") from e
                
                elif key == "date":
                    try:
                        from datetime import datetime
                        # Parse date string
                        parsed_date = datetime.strptime(value, "%Y-%m-%d")
                        results[key] = parsed_date.strftime("%B %d, %Y")
                    except ValueError as e:
                        raise ValueError(f"Invalid date format in {key}: {e}") from e
                
                else:
                    # Default processing
                    results[key] = str(value).upper()
            
            except ValueError as e:
                print(f"  Warning: Skipping {key} - {e}")
                results[key] = None
        
        return results
    
    except TypeError as e:
        print(f"Type error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Test complex processing
test_datasets = [
    {"numbers": ["1", "2", "3"], "date": "2025-01-01", "name": "alice"},
    {"numbers": ["1", "abc", "3"], "date": "invalid-date", "name": "bob"},
    {"numbers": [1, 2, 3], "date": "2025-12-25", "status": "active"},
    "not a dictionary",
    {"empty": []}
]

for i, dataset in enumerate(test_datasets, 1):
    print(f"\n--- Dataset {i} ---")
    result = complex_data_processing(dataset)
    print(f"Result: {result}")

print()

# 11. Exception handling best practices
print("11. Best practices demonstration:")

# Good: Specific exception handling
def good_file_reader(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return ""
    except PermissionError:
        print(f"Permission denied for {filename}")
        return ""
    except UnicodeDecodeError:
        print(f"Cannot decode {filename}")
        return ""

# Bad: Catching all exceptions (don't do this)
def bad_file_reader(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except Exception:  # Too broad!
        print("Something went wrong")
        return ""

# Demonstration of logging exceptions
import logging
logging.basicConfig(level=logging.INFO)

def logged_operation(operation_name, func, *args):
    try:
        result = func(*args)
        logging.info(f"{operation_name} completed successfully")
        return result
    except Exception as e:
        logging.error(f"{operation_name} failed: {type(e).__name__}: {e}")
        return None

# Test logging
def risky_calculation(x, y):
    return x / y

operations = [
    ("Division", risky_calculation, 10, 2),
    ("Division by zero", risky_calculation, 10, 0),
]

for name, func, *args in operations:
    result = logged_operation(name, func, *args)
    print(f"{name} result: {result}")

print()

# 12. Summary of exception types
print("12. Common Python exception types:")
exception_examples = {
    "ValueError": "int('abc')",
    "TypeError": "'hello' + 5",
    "IndexError": "[1, 2, 3][10]",
    "KeyError": "{'a': 1}['b']",
    "AttributeError": "'hello'.nonexistent_method()",
    "ZeroDivisionError": "10 / 0",
    "FileNotFoundError": "open('nonexistent.txt')",
    "ImportError": "import nonexistent_module"
}

for exc_type, example in exception_examples.items():
    print(f"{exc_type:20}: {example}")

print("\nException handling guidelines:")
print("✓ Catch specific exceptions, not general Exception")
print("✓ Handle exceptions at the appropriate level")
print("✓ Use finally for cleanup code")
print("✓ Don't ignore exceptions silently")
print("✓ Log exceptions for debugging")
print("✓ Use custom exceptions for domain-specific errors")
print("✓ Document what exceptions your functions can raise")
