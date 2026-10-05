# =====================================================
# POINT 1: WHAT IS A STRING?
# =====================================================

# A string is an immutable sequence of characters
s = "python"

print(s)                 # python
print(type(s))           # <class 'str'>


# =====================================================
# POINT 2: CREATING STRINGS
# =====================================================

# Single quotes
s1 = 'hello'

# Double quotes
s2 = "hello"

# Triple quotes (multi-line string)
s3 = """This is
a multi-line
string"""

print(s1)
print(s2)
print(s3)


# =====================================================
# POINT 3: INDEXING & SLICING
# =====================================================

word = "python"

# Indexing (0-based)
print(word[0])           # p
print(word[1])           # y
print(word[-1])          # n (negative indexing)

# Slicing: start : end : step
print(word[1:4])         # yth
print(word[:3])          # pyt
print(word[3:])          # hon
print(word[::-1])        # nohtyp (reverse string)

# Slicing is safe even if index is out of range
print(word[0:100])       # python


# =====================================================
# POINT 4: STRINGS ARE IMMUTABLE
# =====================================================

text = "hello"

# ❌ This is NOT allowed (will cause error if uncommented)
# text[0] = "H"

# ✅ Correct way: create a NEW string
text = "H" + text[1:]

print(text)              # Hello


# =====================================================
# POINT 5: LOOPING OVER STRINGS
# =====================================================

name = "Rishu"

# Loop character by character
for ch in name:
    print(ch)

# Strings are iterable (like lists, but immutable)


# =====================================================
# POINT 6: MEMBERSHIP OPERATORS
# =====================================================

sentence = "python programming"

# Only two membership operators exist: in, not in
print("python" in sentence)       # True (substring check)
print("java" in sentence)         # False
print("py" in sentence)           # True
print("x" not in sentence)        # True

# Membership is case-sensitive
print("Python" in sentence)       # False


# =====================================================
# POINT 7: LENGTH & BASIC TYPE CONVERSION
# =====================================================

print(len("hello"))       # 5

# Type conversions
num_str = "42"
num = int(num_str)
flt = float("3.14")
back_to_str = str(100)

print(num, type(num))             # 42 <class 'int'>
print(flt, type(flt))             # 3.14 <class 'float'>
print(back_to_str, type(back_to_str))  # "100" <class 'str'>


# =====================================================
# POINT 8: STRING CONCATENATION
# =====================================================

# Concatenation
print("hello" + " world")          # hello world

# Repetition
print("ha" * 3)                    # hahaha

# ⚠️ Avoid + in large loops (performance issue – see point 17)


# =====================================================
# POINT 9: f-STRINGS (BEST WAY TO FORMAT)
# =====================================================

name = "Rishu"
age = 20

# f-string inserts variables directly
print(f"My name is {name} and I am {age} years old")

# Expressions inside f-strings
print(f"Next year I will be {age + 1}")

# f-strings return strings
formatted = f"{10 + 5}"
print(formatted, type(formatted))   # "15" <class 'str'>


# =====================================================
# POINT 10: COMMON STRING METHODS
# =====================================================

s = "  hello world  "

# ---- Case conversion ----
print(s.upper())          # "  HELLO WORLD  "
print(s.lower())          # "  hello world  "
print(s.capitalize())     # "  hello world  "
print(s.title())          # "  Hello World  "

# ---- Whitespace removal ----
print(s.strip())          # "hello world"
print(s.lstrip())         # "hello world  "
print(s.rstrip())         # "  hello world"

# ---- Replace ----
print(s.replace("world", "python"))  # "  hello python  "

# ---- Starts / Ends with ----
print(s.startswith("  he"))          # True
print(s.endswith("  "))              # True

# IMPORTANT:
# None of these methods modify the original string
print(s)                  # "  hello world  " (unchanged)


# ============================
# POINT 11: FINDING & COUNTING
# ============================



text = "hello world"

# find() returns the starting index of the substring
print(text.find("world"))   # Output: 6

# If substring is not found, find() returns -1 (NO error)
print(text.find("python"))  # Output: -1

# find() is case-sensitive
print(text.find("World"))   # Output: -1

# find() with start index
print(text.find("o", 5))    # Output: 7 (search starts from index 5)

# count() returns number of non-overlapping occurrences
print(text.count("l"))      # Output: 3

# time complexity of find() and count is O(n)

# ============================
# POINT 12: SPLIT & JOIN
# ============================

data = "apple,banana,grape"

# split() breaks string into a list
fruits = data.split(",")

print(fruits)               # ['apple', 'banana', 'grape']
print(data)                 # Original string unchanged

# Default split() splits on whitespace
sentence = "  hello   world  python "
words = sentence.split()

print(words)                # ['hello', 'world', 'python']

# join() joins list elements into a string
joined = " | ".join(words)

print(joined)               # hello | world | python
print(words)                # Original list unchanged


# ============================
# POINT 13: ESCAPE CHARACTERS
# ============================

# \n -> new line
print("hello\nworld")

# \t -> tab
print("hello\tworld")

# Escaping quotes
print("He said \"hello\"")

# Raw string (ignores escape characters)
print(r"C:\new\test")       # Backslashes printed as-is


# ============================
# POINT 14: STRING VALIDATION METHODS
# ============================

s1 = "Python"
s2 = "12345"
s3 = "Python123"
s4 = "   "

print(s1.isalpha())         # True (only letters)
print(s2.isdigit())         # True (only digits)
print(s3.isalnum())         # True (letters + digits)
print(s4.isspace())         # True (only whitespace)

print("hello".islower())    # True
print("HELLO".isupper())    # True


# ============================
# POINT 15: STRING COMPARISON
# ============================

# Equality comparison
print("apple" == "apple")   # True  # noqa: PLR0133
print("apple" == "Apple")   # False (case-sensitive)  # noqa: PLR0133

# Lexicographical comparison (ASCII-based)
print("a" < "b")            # True  # noqa: PLR0133
print("A" < "a")            # True ('A' has smaller ASCII value)  # noqa: PLR0133


# ============================
# POINT 16: TYPE CONVERSION
# ============================

num_str = "10"
float_str = "3.14"

# String to int
num = int(num_str)
print(num, type(num))       # 10 <class 'int'>

# String to float
flt = float(float_str)
print(flt, type(flt))       # 3.14 <class 'float'>

# Number to string
num_to_str = str(100)
print(num_to_str, type(num_to_str))  # "100" <class 'str'>


# ============================
# POINT 17: PERFORMANCE (VERY IMPORTANT)
# ============================

# ❌ BAD WAY: string concatenation in loop
bad_string = ""

for i in range(5):
    bad_string += str(i)    # creates a NEW string every time

print(bad_string)           # 01234


# ✅ GOOD WAY: list + join
parts = []

for i in range(5):
    parts.append(str(i))    # list append is efficient

good_string = "".join(parts)

print(good_string)          # 01234
