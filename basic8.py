"""
PYTHON EXCEPTION HANDLING - COMPLETE SUMMARY
=============================================

This file demonstrates all key exception handling concepts with executable examples.
Run this file to see all concepts in action!
"""

print("=" * 70)
print("PYTHON EXCEPTION HANDLING - INTERACTIVE EXAMPLES")
print("=" * 70)


# ============================================================================
# 1. WHAT ARE EXCEPTIONS?
# ============================================================================
print("\n" + "=" * 70)
print("1. WHAT ARE EXCEPTIONS?")
print("=" * 70)
print("Exceptions are events that disrupt normal program flow")
print("If not handled, the program crashes\n")

# Demonstrating without exception handling would crash:
print("Example: Without handling, this would crash:")
print("  result = 10 / 0  # ZeroDivisionError")
print("\nWith handling:")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("  ✓ Caught ZeroDivisionError - program continues!")


# ============================================================================
# 2. BASIC TRY-EXCEPT
# ============================================================================
print("\n" + "=" * 70)
print("2. BASIC TRY-EXCEPT")
print("=" * 70)
print("Catches exceptions to prevent crashes\n")

# Simulated example (no input required for demo)
print("Example: Catching any exception")
try:
    number = int("not_a_number")
    result = 10 / number
except:
    print("  ✓ Something went wrong! (Caught with bare except)")


# ============================================================================
# 3. CATCHING SPECIFIC EXCEPTIONS (BEST PRACTICE)
# ============================================================================
print("\n" + "=" * 70)
print("3. CATCHING SPECIFIC EXCEPTIONS (BEST PRACTICE)")
print("=" * 70)
print("Catch only the exceptions you expect\n")

print("Example 1: ValueError")
try:
    number = int("hello")
except ValueError:
    print("  ✓ That's not a valid number!")

print("\nExample 2: ZeroDivisionError")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("  ✓ You can't divide by zero!")


# ============================================================================
# 4. CATCHING MULTIPLE EXCEPTIONS IN ONE BLOCK
# ============================================================================
print("\n" + "=" * 70)
print("4. CATCHING MULTIPLE EXCEPTIONS IN ONE BLOCK")
print("=" * 70)

print("\nExample: Handling multiple exception types together")
try:
    data = {"name": "Alice"}
    result = data["age"]  # Will raise KeyError
except (ValueError, TypeError, KeyError):
    print("  ✓ One of several exceptions occurred (KeyError)")


# ============================================================================
# 5. ACCESSING THE EXCEPTION OBJECT
# ============================================================================
print("\n" + "=" * 70)
print("5. ACCESSING THE EXCEPTION OBJECT")
print("=" * 70)
print("Use 'as' to get exception details\n")

try:
    age = int("not a number")
except ValueError as e:
    print(f"  Error details: {e}")
    print(f"  Exception type: {type(e).__name__}")


# ============================================================================
# 6. THE ELSE CLAUSE
# ============================================================================
print("\n" + "=" * 70)
print("6. THE ELSE CLAUSE")
print("=" * 70)
print("Runs ONLY if NO exception occurred in try block\n")

print("Example 1: With exception (else won't run)")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("  ✓ Cannot divide by zero!")
else:
    print("  This won't print")

print("\nExample 2: Without exception (else will run)")
try:
    result = 10 / 2
except ZeroDivisionError:
    print("  Cannot divide by zero!")
else:
    print(f"  ✓ Success! Result is {result}")


# ============================================================================
# 7. THE FINALLY CLAUSE
# ============================================================================
print("\n" + "=" * 70)
print("7. THE FINALLY CLAUSE")
print("=" * 70)
print("ALWAYS executes, regardless of exceptions\n")

print("Example: finally runs even with exception")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("  Exception occurred!")
finally:
    print("  ✓ Finally block ALWAYS runs - used for cleanup")


# ============================================================================
# 8. COMPLETE STRUCTURE (ALL CLAUSES TOGETHER)
# ============================================================================
print("\n" + "=" * 70)
print("8. COMPLETE STRUCTURE (ALL CLAUSES TOGETHER)")
print("=" * 70)
print("Demonstration of try-except-else-finally\n")

print("EXECUTION FLOW:")
print("  1. try block executes")
print("  2. If exception: matching except runs")
print("  3. If NO exception: else runs")
print("  4. finally ALWAYS runs")
print("  5. Only ONE except block executes (first match)")
print()

def demo_complete_structure(value):
    """Shows all clauses in action"""
    print(f"Testing with value: {value}")
    try:
        result = 10 / value
    except ZeroDivisionError:
        print("  ✓ Exception caught: Cannot divide by zero")
    except TypeError:
        print("  ✓ Exception caught: Wrong type")
    else:
        print(f"  ✓ Else: Success! Result = {result}")
    finally:
        print("  ✓ Finally: Always runs")

demo_complete_structure(2)   # Success case
print()
demo_complete_structure(0)   # Exception case


# ============================================================================
# 9. COMMON BUILT-IN EXCEPTIONS
# ============================================================================
print("\n" + "=" * 70)
print("9. COMMON BUILT-IN EXCEPTIONS")
print("=" * 70)

print("\nValueError - Correct type, wrong value")
try:
    age = int("twenty")
except ValueError:
    print("  ✓ ValueError: Invalid value for conversion")

print("\nTypeError - Wrong type for operation")
try:
    result = "hello" + 5
except TypeError:
    print("  ✓ TypeError: Incompatible types")

print("\nKeyError - Dictionary key doesn't exist")
user = {"name": "Alice"}
try:
    email = user["email"]
except KeyError:
    print("  ✓ KeyError: Key not found")

print("\nIndexError - List index out of range")
numbers = [1, 2, 3]
try:
    value = numbers[10]
except IndexError:
    print("  ✓ IndexError: Index out of range")

print("\nFileNotFoundError - File doesn't exist")
try:
    file = open("nonexistent.txt")
except FileNotFoundError:
    print("  ✓ FileNotFoundError: File not found")

print("\nZeroDivisionError - Division by zero")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("  ✓ ZeroDivisionError: Cannot divide by zero")

print("\nAttributeError - Object doesn't have attribute")
try:
    text = "hello"
    text.append("!")
except AttributeError:
    print("  ✓ AttributeError: Attribute doesn't exist")

print("\nModuleNotFoundError - Can't import module")



# ============================================================================
# 10. RAISING EXCEPTIONS
# ============================================================================
print("\n" + "=" * 70)
print("10. RAISING EXCEPTIONS")
print("=" * 70)
print("Create and raise your own exceptions\n")

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return age

print("Example: Raising ValueError for invalid input")
try:
    set_age(-5)
except ValueError as e:
    print(f"  ✓ Caught: {e}")


print("\nCHOOSING THE RIGHT EXCEPTION TYPE:")

# ValueError example
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

print("\n  ValueError - wrong value")
try:
    validate_age(-1)
except ValueError as e:
    print(f"    ✓ {e}")

# TypeError example
def validate_name(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")

print("\n  TypeError - wrong type")
try:
    validate_name(123)
except TypeError as e:
    print(f"    ✓ {e}")

# KeyError example
def get_value(data, key):
    if key not in data:
        raise KeyError(f"Required key '{key}' not found")
    return data[key]

print("\n  KeyError - missing key")
try:
    get_value({"name": "Alice"}, "age")
except KeyError as e:
    print(f"    ✓ {e}")


# ============================================================================
# 11. BEST PRACTICES
# ============================================================================
print("\n" + "=" * 70)
print("11. BEST PRACTICES")
print("=" * 70)

print("\n✓ DO: Be specific about exceptions")
try:
    int("not_a_number")
except ValueError as e:
    print(f"  Specific exception caught: {type(e).__name__}")

print("\n✗ DON'T: Use bare except (catches everything!)")
print("  try:")
print("      risky_code()")
print("  except:  # BAD - catches KeyboardInterrupt, SystemExit, etc.")
print("      pass")

print("\n✓ DO: Keep try blocks small")
print("  Wrap only the code that might raise exceptions")

print("\n✓ DO: Provide helpful error messages")
def withdraw(amount, balance):
    if amount > balance:
        raise ValueError(f"Insufficient funds: need ${amount}, have ${balance}")

try:
    withdraw(100, 50)
except ValueError as e:
    print(f"  ✓ {e}")


# ============================================================================
# 12. PRACTICAL EXAMPLE
# ============================================================================
print("\n" + "=" * 70)
print("12. PRACTICAL EXAMPLE - COMPLETE FUNCTION")
print("=" * 70)
print("Using all exception handling features together\n")

def divide_numbers(a, b):
    """Complete example using all exception handling features."""
    result = None
    
    try:
        print(f"  Attempting to divide {a} by {b}")
        result = a / b
        print("  Division successful")
        
    except ZeroDivisionError:
        print("  Error: Cannot divide by zero")
        result = float('inf')
        
    except TypeError as e:
        print(f"  Error: Invalid types - {e}")
        result = None
        
    else:
        print(f"  Result calculated: {result}")
        if result > 1000:
            print("  Warning: Result is very large")
            
    finally:
        print("  Cleanup: Operation complete")
    
    return result


print("Test 1: Normal division")
divide_numbers(10, 2)

print("\nTest 2: Division by zero")
divide_numbers(10, 0)

print("\nTest 3: Invalid types")
divide_numbers("10", "2")


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
print("\n" + "=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print("""
1. Exceptions prevent crashes by handling errors gracefully
2. Use try-except to catch and handle exceptions
3. Be specific - catch only exceptions you expect
4. Access exception object with 'as e' for details
5. else runs only if NO exception occurred
6. finally ALWAYS runs - use for cleanup
7. raise exceptions to signal errors in your code
8. Choose appropriate exception types (ValueError, TypeError, etc.)
9. Keep try blocks small and focused
10. Use context managers (with) when possible

EXECUTION ORDER:
try → except (if error) OR else (if success) → finally (always)
""")

print("=" * 70)
print("END OF EXCEPTION HANDLING SUMMARY")
print("=" * 70)

