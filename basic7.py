"""
PYTHON TUPLES - COMPLETE REFERENCE GUIDE
==========================================
Everything about tuples in one place for quick revision
"""

# ============================================================================
# SECTION 1: CREATING TUPLES
# ============================================================================

print("=" * 60)
print("SECTION 1: CREATING TUPLES")
print("=" * 60)

# Empty tuple
empty = ()
empty2 = tuple()

# Single element (comma is REQUIRED!)
single = (5,)  # Correct
not_tuple = (5)  # This is just an integer!

# Multiple elements
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

# Tuple packing (no parentheses)
coords = 10, 20, 30

# From other iterables
from_list = tuple([1, 2, 3])
from_string = tuple("abc")  # ('a', 'b', 'c')

print(f"Single element tuple: {single}")
print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")
print(f"From string: {from_string}")

# ============================================================================
# SECTION 2: ACCESSING ELEMENTS
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 2: ACCESSING ELEMENTS")
print("=" * 60)

fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Indexing
print(f"First: {fruits[0]}")
print(f"Last: {fruits[-1]}")

# Slicing
print(f"Middle elements [1:3]: {fruits[1:3]}")
print(f"First two: {fruits[:2]}")
print(f"From index 2: {fruits[2:]}")
print(f"Every 2nd element: {fruits[::2]}")
print(f"Reversed: {fruits[::-1]}")

# ============================================================================
# SECTION 3: TUPLE OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 3: TUPLE OPERATIONS")
print("=" * 60)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(f"Concatenation: {tuple1} + {tuple2} = {combined}")

# Repetition
repeated = (1, 2) * 3
print(f"Repetition: (1, 2) * 3 = {repeated}")

# Membership
print(f"2 in {tuple1}: {2 in tuple1}")
print(f"10 not in {tuple1}: {10 not in tuple1}")

# Length
print(f"Length of {tuple1}: {len(tuple1)}")

# ============================================================================
# SECTION 4: TUPLE METHODS (Only 2!)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 4: TUPLE METHODS")
print("=" * 60)

numbers = (1, 2, 3, 2, 4, 2, 5)

# count() - count occurrences
print(f"Count of 2 in {numbers}: {numbers.count(2)}")

# index() - find first occurrence
print(f"First index of 4: {numbers.index(4)}")
print(f"First index of 2: {numbers.index(2)}")

# ============================================================================
# SECTION 5: IMMUTABILITY
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 5: IMMUTABILITY")
print("=" * 60)

my_tuple = (1, 2, 3)
print(f"Original: {my_tuple}")

# Cannot modify
# my_tuple[0] = 10  # TypeError!

# Can create new tuples
my_tuple = my_tuple + (4, 5)
print(f"New tuple: {my_tuple}")

# Tuples with mutable objects
mixed = ([1, 2], [3, 4])
mixed[0].append(3)  # Modifying the list inside works!
print(f"Modified list inside tuple: {mixed}")
# mixed[0] = [5, 6]  # This fails! Can't reassign

# ============================================================================
# SECTION 6: UNPACKING TUPLES
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 6: UNPACKING TUPLES")
print("=" * 60)

# Basic unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")

# Extended unpacking with *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"first={first}, middle={middle}, last={last}")

# Swapping variables
a, b = 5, 10
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Ignoring values
name, _, age = ("Alice", "middle", 25)
print(f"name={name}, age={age}")

# Nested unpacking
people = (("Alice", 25), ("Bob", 30))
for name, age in people:
    print(f"{name} is {age} years old")

# ============================================================================
# SECTION 7: LOOPING THROUGH TUPLES
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 7: LOOPING THROUGH TUPLES")
print("=" * 60)

fruits = ("apple", "banana", "cherry")

# Direct iteration
print("Direct iteration:")
for fruit in fruits:
    print(f"  {fruit}")

# With index using enumerate()
print("\nWith enumerate:")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")

# Looping multiple tuples with zip()
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)
print("\nUsing zip:")
for name, age in zip(names, ages):
    print(f"  {name} is {age}")

# Reversed iteration
print("\nReversed:")
for fruit in reversed(fruits):
    print(f"  {fruit}")

# Nested tuple iteration
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("\nNested iteration:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

# Unpacking in loops
print("\nUnpacking tuples in loops:")
coordinates = ((0, 0), (1, 2), (3, 4))
for x, y in coordinates:
    print(f"  Point at ({x}, {y})")

# Unpacking nested tuples in loops
people = (
    ("Alice", (25, "Engineer")),
    ("Bob", (30, "Designer")),
    ("Charlie", (35, "Manager"))
)
print("\nUnpacking nested tuples:")
for name, (age, job) in people:
    print(f"  {name}: {age} years old, works as {job}")

# Unpacking with enumerate
print("\nUnpacking with enumerate:")
scores = ((85, 90), (78, 82), (92, 88))
for index, (test1, test2) in enumerate(scores, start=1):
    avg = (test1 + test2) / 2
    print(f"  Student {index}: Test1={test1}, Test2={test2}, Avg={avg}")

# Unpacking with zip
print("\nUnpacking with zip:")
locations = (("NYC", "London"), ("Paris", "Tokyo"))
populations = ((8.3, 9.0), (2.1, 13.9))
for (city1, city2), (pop1, pop2) in zip(locations, populations):
    print(f"  {city1}: {pop1}M, {city2}: {pop2}M")

# ============================================================================
# SECTION 8: SORTING TUPLES
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 8: SORTING TUPLES")
print("=" * 60)

numbers = (5, 2, 8, 1, 9, 3)

# Basic sorting (returns list, convert back to tuple)
sorted_tuple = tuple(sorted(numbers))
print(f"Sorted: {sorted_tuple}")

# Descending order
descending = tuple(sorted(numbers, reverse=True))
print(f"Descending: {descending}")

# Sorting tuples of tuples
students = [
    ("Alice", 85, 22),
    ("Bob", 92, 20),
    ("Charlie", 78, 21),
    ("David", 92, 19)
]

print("\nSorting by score (index 1):")
by_score = sorted(students, key=lambda x: x[1])
for student in by_score:
    print(f"  {student}")

# Multi-level sorting (score desc, then age asc)
print("\nMulti-level sort (score↓, age↑):")
multi_sort = sorted(students, key=lambda x: (-x[1], x[2]))
for student in multi_sort:
    print(f"  {student}")

# Using itemgetter (more efficient)
from operator import itemgetter
by_age = sorted(students, key=itemgetter(2))
print("\nSorted by age using itemgetter:")
for student in by_age:
    print(f"  {student}")

# ============================================================================
# SECTION 9: COMPARING TUPLES
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 9: COMPARING TUPLES")
print("=" * 60)

# Lexicographic comparison
print(f"(1, 2, 3) < (1, 2, 4): {(1, 2, 3) < (1, 2, 4)}")
print(f"(2, 0) > (1, 100): {(2, 0) > (1, 100)}")
print(f"(1, 2) == (1, 2): {(1, 2) == (1, 2)}")

# ============================================================================
# SECTION 10: TUPLES VS LISTS
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 10: TUPLES VS LISTS")
print("=" * 60)

import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(my_list)} bytes")
print(f"Tuple size: {sys.getsizeof(my_tuple)} bytes")

# Tuples as dictionary keys (lists can't!)
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}
print(f"\nTuples as dict keys: {locations[(40.7128, -74.0060)]}")

# Tuples in sets
coords_set = {(0, 0), (1, 1), (2, 2)}
print(f"Tuples in sets: {coords_set}")

# ============================================================================
# SECTION 11: TUPLE "COMPREHENSIONS" (Generator Expressions)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 11: CREATING TUPLES FROM GENERATORS")
print("=" * 60)

# No true tuple comprehension! Use generator expression
gen = (x**2 for x in range(5))
print(f"Generator object: {gen}")
print(f"Generator type: {type(gen)}")

# Convert to tuple
squares = tuple(x**2 for x in range(5))
print(f"Squares tuple: {squares}")

# Filter and create tuple
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
evens = tuple(x for x in numbers if x % 2 == 0)
print(f"Even numbers: {evens}")

# Transform and create tuple
words = ("hello", "world", "python")
uppercase = tuple(word.upper() for word in words)
print(f"Uppercase: {uppercase}")

# Nested iteration
matrix = ((1, 2), (3, 4), (5, 6))
flattened = tuple(num for row in matrix for num in row)
print(f"Flattened: {flattened}")

# ============================================================================
# SECTION 12: PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 12: PRACTICAL EXAMPLES")
print("=" * 60)

# 1. Returning multiple values from functions
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

data = [10, 20, 30, 40, 50]
minimum, maximum, average = get_stats(data)
print(f"Stats: min={minimum}, max={maximum}, avg={average}")

# 2. Database-like records
employees = [
    ("Alice", 30, "Engineering"),
    ("Bob", 25, "Marketing"),
    ("Charlie", 35, "Sales")
]

print("\nEmployees:")
for name, age, dept in employees:
    print(f"  {name} ({age}) - {dept}")

# 3. Configuration tuples
CONFIG = ("localhost", 8080, True)
host, port, debug = CONFIG
print(f"\nConfig: host={host}, port={port}, debug={debug}")

# 4. Coordinates and points
points = [(0, 0), (3, 4), (6, 8)]
print("\nDistances from origin:")
for x, y in points:
    distance = (x**2 + y**2) ** 0.5
    print(f"  ({x}, {y}) -> {distance:.2f}")

# ============================================================================
# SECTION 13: ADVANCED UNPACKING - *args and **kwargs
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 13: ADVANCED UNPACKING - *args and **kwargs")
print("=" * 60)

# Extended unpacking with * in assignment
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"Extended unpacking: first={first}, middle={middle}, last={last}")
print(f"Note: middle is a {type(middle).__name__}!")

# Unpacking in function calls
def calculate(x, y, z):
    return x + y + z

point = (5, 10, 15)
result = calculate(*point)  # Spreads tuple into separate arguments
print(f"\ncalculate(*point) = {result}")
print("*point unpacks to: calculate(5, 10, 15)")

# Combining tuples with *
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = (*tuple1, *tuple2)
print(f"\nCombined tuples: {combined}")

# *args - Variable positional arguments (collects into tuple)
def greet(*names):
    print(f"\ngreet() received {len(names)} arguments as tuple")
    for name in names:
        print(f"  Hello, {name}!")

greet("Alice", "Bob", "Charlie")

# Mixing regular parameters with *args
def sum_all(*numbers):
    return sum(numbers)

print(f"\nsum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

# **kwargs - Variable keyword arguments (collects into dict)
def print_info(**details):
    print(f"\nprint_info() received keyword arguments as dict:")
    for key, value in details.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=25, city="NYC")

# Unpacking dictionary with **
def create_user(name, age, email):
    return f"User: {name}, {age}, {email}"

user_data = {"name": "Bob", "age": 30, "email": "bob@example.com"}
result = create_user(**user_data)  # Unpacks dict to keyword arguments
print(f"\ncreate_user(**user_data) = {result}")

# Combining all together
def full_function(required, *args, **kwargs):
    print(f"\nRequired: {required}")
    print(f"Args (tuple): {args}")
    print(f"Kwargs (dict): {kwargs}")

full_function(1, 2, 3, 4, name="Alice", age=25)

print("\nKey Points:")
print("  • * in assignment → captures into LIST")
print("  • * in function call → SPREADS into arguments")
print("  • *args as parameter → collects into TUPLE")
print("  • **kwargs as parameter → collects into DICT")
print("  • ** in function call → unpacks dict to keyword args")

print("\n" + "=" * 60)
print("END OF TUPLE REFERENCE GUIDE")
print("=" * 60)