"""
Python Workshop - 10: Workshop Summary and Practice Exercises
============================================================

This file contains a summary of all topics and practice exercises.
"""

print("=" * 60)
print("PYTHON WORKSHOP SUMMARY")
print("=" * 60)

# Topic 1: Python Syntax Overview
print("\n1. PYTHON SYNTAX OVERVIEW")
print("-" * 30)
print("✓ Variables and basic data types")
print("✓ Print statements and string formatting")
print("✓ Basic operators (arithmetic, comparison, logical)")
print("✓ Functions and parameters")
print("✓ Indentation and code blocks")

# Topic 2: Data Types - Lists
print("\n2. LISTS")
print("-" * 10)
print("✓ Creating and accessing lists")
print("✓ List methods: append(), insert(), remove(), pop()")
print("✓ Slicing and indexing")
print("✓ List comprehensions")
print("✓ Nested lists")

# Topic 3: Data Types - Dictionaries
print("\n3. DICTIONARIES")
print("-" * 15)
print("✓ Key-value pairs")
print("✓ Dictionary methods: keys(), values(), items()")
print("✓ Adding, updating, and removing elements")
print("✓ Dictionary comprehensions")
print("✓ Nested dictionaries")

# Topic 4: Data Types - Sets
print("\n4. SETS")
print("-" * 8)
print("✓ Unique elements only")
print("✓ Set operations: union, intersection, difference")
print("✓ Adding and removing elements")
print("✓ Set comprehensions")
print("✓ Membership testing")

# Topic 5: Data Types - Tuples
print("\n5. TUPLES")
print("-" * 10)
print("✓ Immutable sequences")
print("✓ Tuple unpacking")
print("✓ Multiple assignment")
print("✓ Named tuples")
print("✓ Use cases for tuples")

# Topic 6: Control Flow - If Statements
print("\n6. IF STATEMENTS")
print("-" * 16)
print("✓ Basic if-elif-else structure")
print("✓ Logical operators (and, or, not)")
print("✓ Comparison operators")
print("✓ Membership and identity operators")
print("✓ Conditional expressions (ternary operator)")

# Topic 7: Control Flow - For Loops
print("\n7. FOR LOOPS")
print("-" * 12)
print("✓ Iterating over sequences")
print("✓ Range function")
print("✓ Enumerate for index-value pairs")
print("✓ Zip for multiple sequences")
print("✓ Loop control: break, continue")
print("✓ For-else construct")

# Topic 8: Control Flow - While Loops
print("\n8. WHILE LOOPS")
print("-" * 14)
print("✓ Condition-based iteration")
print("✓ Loop control: break, continue")
print("✓ While-else construct")
print("✓ Input validation patterns")
print("✓ Avoiding infinite loops")

# Topic 9: Exception Handling
print("\n9. EXCEPTION HANDLING")
print("-" * 20)
print("✓ Try-except blocks")
print("✓ Multiple exception types")
print("✓ Else and finally clauses")
print("✓ Custom exceptions")
print("✓ Exception chaining")

print("\n" + "=" * 60)
print("PRACTICE EXERCISES")
print("=" * 60)

# Exercise 1: List Operations
print("\nEXERCISE 1: List Operations")
print("-" * 30)
print("Create a program that:")
print("1. Creates a list of numbers from 1 to 10")
print("2. Filters even numbers using list comprehension")
print("3. Calculates the sum and average of even numbers")
print("4. Finds the maximum and minimum values")

def exercise_1():
    # Solution
    numbers = list(range(1, 11))
    even_numbers = [x for x in numbers if x % 2 == 0]
    total = sum(even_numbers)
    average = total / len(even_numbers)
    maximum = max(even_numbers)
    minimum = min(even_numbers)
    
    print(f"Numbers: {numbers}")
    print(f"Even numbers: {even_numbers}")
    print(f"Sum: {total}, Average: {average}")
    print(f"Max: {maximum}, Min: {minimum}")

exercise_1()

# Exercise 2: Dictionary Student Management
print("\nEXERCISE 2: Student Management System")
print("-" * 40)
print("Create a program that manages student grades:")

def exercise_2():
    students = {
        "Alice": [85, 92, 78, 96],
        "Bob": [76, 88, 82, 94],
        "Charlie": [95, 87, 91, 89],
        "Diana": [82, 79, 88, 91]
    }
    
    print("Student Grade Report:")
    print("-" * 40)
    
    for name, grades in students.items():
        average = sum(grades) / len(grades)
        highest = max(grades)
        lowest = min(grades)
        
        # Determine letter grade
        if average >= 90:
            letter = "A"
        elif average >= 80:
            letter = "B"
        elif average >= 70:
            letter = "C"
        else:
            letter = "F"
        
        print(f"{name:10} | Avg: {average:5.1f} | Grade: {letter} | High: {highest} | Low: {lowest}")

exercise_2()

# Exercise 3: Set Operations
print("\nEXERCISE 3: Set Operations")
print("-" * 25)
print("Analyze common elements between different groups:")

def exercise_3():
    python_students = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
    java_students = {"Bob", "Charlie", "Frank", "Grace", "Alice"}
    javascript_students = {"Charlie", "Diana", "Frank", "Henry"}
    
    print(f"Python students: {python_students}")
    print(f"Java students: {java_students}")
    print(f"JavaScript students: {javascript_students}")
    
    # Students taking all three languages
    all_three = python_students & java_students & javascript_students
    print(f"\nStudents in all three: {all_three}")
    
    # Students in Python or Java but not JavaScript
    py_or_java_not_js = (python_students | java_students) - javascript_students
    print(f"Python or Java but not JavaScript: {py_or_java_not_js}")
    
    # Students in exactly one language
    only_python = python_students - java_students - javascript_students
    only_java = java_students - python_students - javascript_students
    only_js = javascript_students - python_students - java_students
    print(f"Only Python: {only_python}")
    print(f"Only Java: {only_java}")
    print(f"Only JavaScript: {only_js}")

exercise_3()

# Exercise 4: Tuple Coordinates
print("\nEXERCISE 4: Coordinate System")
print("-" * 30)
print("Work with coordinate points using tuples:")

def exercise_4():
    points = [(0, 0), (3, 4), (1, 1), (5, 12), (8, 6)]
    
    print(f"Points: {points}")
    
    # Calculate distances from origin
    distances = []
    for x, y in points:
        distance = (x**2 + y**2)**0.5
        distances.append((distance, (x, y)))
    
    # Sort by distance
    distances.sort()
    
    print("\nPoints sorted by distance from origin:")
    for distance, point in distances:
        print(f"Point {point}: {distance:.2f}")
    
    # Find quadrants
    quadrants = {1: [], 2: [], 3: [], 4: []}
    origin = []
    
    for x, y in points:
        if x == 0 and y == 0:
            origin.append((x, y))
        elif x > 0 and y > 0:
            quadrants[1].append((x, y))
        elif x < 0 and y > 0:
            quadrants[2].append((x, y))
        elif x < 0 and y < 0:
            quadrants[3].append((x, y))
        elif x > 0 and y < 0:
            quadrants[4].append((x, y))
    
    print("\nPoints by quadrant:")
    for quad, pts in quadrants.items():
        if pts:
            print(f"Quadrant {quad}: {pts}")
    if origin:
        print(f"Origin: {origin}")

exercise_4()

# Exercise 5: Control Flow - Number Guessing Game
print("\nEXERCISE 5: Number Guessing Game Logic")
print("-" * 40)

def exercise_5():
    import random
    
    def play_guessing_game(secret_number, max_attempts=5):
        # Simulate guesses for demonstration
        possible_guesses = [1, 5, 7, 8, 6]
        
        print(f"Secret number: {secret_number} (1-10)")
        print(f"Maximum attempts: {max_attempts}")
        
        for attempt in range(1, max_attempts + 1):
            if attempt <= len(possible_guesses):
                guess = possible_guesses[attempt - 1]
            else:
                guess = random.randint(1, 10)
            
            print(f"Attempt {attempt}: Guess = {guess}")
            
            if guess == secret_number:
                print(f"🎉 Correct! Found it in {attempt} attempts!")
                return True
            elif guess < secret_number:
                print("   Too low!")
            else:
                print("   Too high!")
        
        print(f"😞 Game over! The number was {secret_number}")
        return False
    
    # Play a few games
    secret = random.randint(1, 10)
    play_guessing_game(secret)

exercise_5()

# Exercise 6: Exception Handling - Safe Calculator
print("\nEXERCISE 6: Safe Calculator")
print("-" * 30)

def exercise_6():
    def safe_calculator(expression):
        """
        Safely evaluate mathematical expressions
        """
        try:
            # Split the expression
            parts = expression.split()
            if len(parts) != 3:
                raise ValueError("Expression must be in format: number operator number")
            
            num1, operator, num2 = parts
            
            # Convert to numbers
            try:
                n1 = float(num1)
                n2 = float(num2)
            except ValueError:
                raise ValueError("Invalid numbers in expression")
            
            # Perform operation
            if operator == "+":
                result = n1 + n2
            elif operator == "-":
                result = n1 - n2
            elif operator == "*":
                result = n1 * n2
            elif operator == "/":
                if n2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = n1 / n2
            elif operator == "**":
                result = n1 ** n2
            else:
                raise ValueError(f"Unsupported operator: {operator}")
            
            return f"{expression} = {result}"
        
        except (ValueError, ZeroDivisionError) as e:
            return f"Error: {e}"
        except Exception as e:
            return f"Unexpected error: {e}"
    
    # Test expressions
    test_expressions = [
        "10 + 5",
        "20 - 8",
        "6 * 7",
        "15 / 3",
        "2 ** 3",
        "10 / 0",
        "abc + 5",
        "10 + + 5",
        "10 % 3"
    ]
    
    print("Calculator Test Results:")
    print("-" * 25)
    for expr in test_expressions:
        result = safe_calculator(expr)
        print(f"{expr:10} -> {result}")

exercise_6()

# Final Challenge
print("\n" + "=" * 60)
print("FINAL CHALLENGE: Text Analysis Tool")
print("=" * 60)

def final_challenge():
    """
    Create a comprehensive text analysis tool that uses all concepts
    """
    
    def analyze_text(text):
        try:
            if not isinstance(text, str):
                raise TypeError("Input must be a string")
            
            if not text.strip():
                raise ValueError("Input cannot be empty")
            
            # Basic statistics
            char_count = len(text)
            word_count = len(text.split())
            sentence_count = text.count('.') + text.count('!') + text.count('?')
            
            # Character analysis
            char_freq = {}
            for char in text.lower():
                if char.isalpha():
                    char_freq[char] = char_freq.get(char, 0) + 1
            
            # Word analysis
            words = [word.strip('.,!?').lower() for word in text.split()]
            word_freq = {}
            for word in words:
                if word:
                    word_freq[word] = word_freq.get(word, 0) + 1
            
            # Find most common
            most_common_char = max(char_freq.items(), key=lambda x: x[1]) if char_freq else None
            most_common_word = max(word_freq.items(), key=lambda x: x[1]) if word_freq else None
            
            # Unique words
            unique_words = set(words)
            
            # Long words (> 5 characters)
            long_words = [word for word in unique_words if len(word) > 5]
            
            # Vowel count
            vowels = set('aeiou')
            vowel_count = sum(1 for char in text.lower() if char in vowels)
            
            # Results
            results = {
                'basic_stats': {
                    'characters': char_count,
                    'words': word_count,
                    'sentences': sentence_count,
                    'unique_words': len(unique_words)
                },
                'character_analysis': {
                    'total_letters': sum(char_freq.values()),
                    'vowel_count': vowel_count,
                    'most_common_char': most_common_char
                },
                'word_analysis': {
                    'most_common_word': most_common_word,
                    'long_words': sorted(long_words),
                    'average_word_length': sum(len(word) for word in words) / len(words) if words else 0
                }
            }
            
            return results
        
        except (TypeError, ValueError) as e:
            return {'error': str(e)}
        except Exception as e:
            return {'error': f'Unexpected error: {e}'}
    
    # Test the analyzer
    sample_texts = [
        "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet!",
        "Python is an amazing programming language. Python makes coding fun and easy.",
        "",
        123,  # Invalid input
        "Short text."
    ]
    
    print("Text Analysis Results:")
    print("=" * 50)
    
    for i, text in enumerate(sample_texts, 1):
        print(f"\nTest {i}: {text!r}")
        print("-" * 30)
        
        result = analyze_text(text)
        
        if 'error' in result:
            print(f"❌ {result['error']}")
        else:
            # Display results
            basic = result['basic_stats']
            char_analysis = result['character_analysis']
            word_analysis = result['word_analysis']
            
            print(f"📊 Basic Stats:")
            print(f"   Characters: {basic['characters']}")
            print(f"   Words: {basic['words']}")
            print(f"   Sentences: {basic['sentences']}")
            print(f"   Unique words: {basic['unique_words']}")
            
            print(f"\n🔤 Character Analysis:")
            print(f"   Total letters: {char_analysis['total_letters']}")
            print(f"   Vowels: {char_analysis['vowel_count']}")
            if char_analysis['most_common_char']:
                char, count = char_analysis['most_common_char']
                print(f"   Most common letter: '{char}' ({count} times)")
            
            print(f"\n📝 Word Analysis:")
            if word_analysis['most_common_word']:
                word, count = word_analysis['most_common_word']
                print(f"   Most common word: '{word}' ({count} times)")
            print(f"   Average word length: {word_analysis['average_word_length']:.1f}")
            if word_analysis['long_words']:
                print(f"   Long words (>5 chars): {', '.join(word_analysis['long_words'][:5])}")

final_challenge()

print("\n" + "=" * 60)
print("🎉 CONGRATULATIONS! 🎉")
print("You've completed the Python Workshop!")
print("=" * 60)
print("\n📚 Topics Covered:")
print("✅ Python syntax and basic operations")
print("✅ Data types: Lists, Dictionaries, Sets, Tuples")
print("✅ Control flow: If statements, For loops, While loops")
print("✅ Exception handling with try-except")
print("\n💡 Next Steps:")
print("• Practice with real projects")
print("• Learn about functions and classes")
print("• Explore Python libraries and frameworks")
print("• Build web applications or data analysis tools")
print("\n🚀 Keep coding and have fun with Python!")
