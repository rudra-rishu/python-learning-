# =====================================================
# POINT 1: WHAT IS A DICTIONARY?
# =====================================================

# A dictionary is a mutable collection of key–value pairs
# Keys are UNIQUE and HASHABLE(immutable)
# Values can be ANY object

d = {"a": 1, "b": 2}

print(d)                 # {'a': 1, 'b': 2}
print(type(d))           # <class 'dict'>


# =====================================================
# POINT 2: CREATING DICTIONARIES (ALL WAYS)
# =====================================================

# 1. Dictionary literal
d1 = {"x": 10, "y": 20}

# 2. Empty dictionary
d2 = {}

# 3. Using dict() constructor
d=dict()  # noqa: C408

# 4. Using keyword arguments (strings here becomes the keys)
d4 = dict(a=1, b=2)  # noqa: C408

# 5. From iterable of key–value pairs- any iterable conataining interable having a pair of elements can make a dictionary where the 1st vaue inside the inner interable  makes the key while the second value makes the value of the dictionary

d6 = dict([["x", 10]]) #here outer iterable - list , inner iterable - tuple , key:x and value:10

# 6. Using zip()
keys = ["k1", "k2"]
values = [100, 200]
d7 = dict(zip(keys, values)) #{"K1":100,"K2":200}

# 7. Dictionary comprehension
d8 = {x: x*x for x in range(3)} #{0:0,1:1,2:4}

# 8. Using fromkeys()
d9 = dict.fromkeys(["a", "b", "c"], 0)#{"a":0,"b":0,"c":0}

print(d1, d4,  d6, d7, d8, d9)


# =====================================================
# POINT 3: RULES FOR KEYS
# =====================================================

# ✅ Keys must be HASHABLE (immutable)
valid_keys = {
    "string": 1,
    10: "int key",
    3.14: "float key",
    (1, 2): "tuple key",
    True: "bool key"
}

print(valid_keys)

# ❌ Invalid keys (uncomment to see error)
# d = {[1, 2]: "list key"}      # TypeError
# d = {{1, 2}: "set key"}       # TypeError
# d = {{"a": 1}: "dict key"}    # TypeError

# ❗ Keys must be UNIQUE
d = {"a": 1, "a": 2}  # noqa: F601
print(d)                       # {'a': 2}

# ❗ True and 1 are SAME key (hash + equality)
d = {True: "yes", 1: "no"}
print(d)                       # {True: 'no'}


# =====================================================
# POINT 4: RULES FOR VALUES
# =====================================================

# Values can be ANY object
d = {
    "int": 10,
    "float": 3.14,
    "list": [1, 2],
    "tuple": (1, 2),
    "dict": {"a": 1},
    "function": len,
    "class": int
}

print(d)

# Values can REPEAT
d = {"a": 1, "b": 1, "c": 1}
print(d)


# =====================================================
# POINT 5: ACCESSING DICTIONARY
# =====================================================

d = {"a": 10, "b": 20, "c": 30}

# Access by key (unsafe)
print(d["a"])                 # 10
# print(d["x"])               # KeyError

# Safe access using get()- this doesn't give error
print(d.get("a"))             # 10
print(d.get("x"))             # None
print(d.get("x", 0))          # 0

# Check key existence
print("a" in d)               # True
print("x" in d)               # False


# =====================================================
# POINT 6: ITERATING OVER DICTIONARY
# =====================================================

# Iterate over keys (default)
for k in d:
    print(k)

# Explicit keys
for k in d.keys():  # noqa: SIM118
    print(k)

# Values
for v in d.values():
    print(v)

# Key + value
for k, v in d.items():
    print(k, v)


# =====================================================
# POINT 7: FIRST & LAST ELEMENT (ORDERED DICT)
# =====================================================

# Python 3.7+ dictionaries preserve insertion order

first_key = next(iter(d))
last_key = next(reversed(d))

print(first_key, d[first_key])   # a 10
print(last_key, d[last_key])     # c 30

first_item = next(iter(d.items()))
last_item = next(reversed(d.items()))

print(first_item)                # ('a', 10)
print(last_item)                 # ('c', 30)


# =====================================================
# POINT 8: ADDING & UPDATING ELEMENTS
# =====================================================

d = {}

# Add new key
d["a"] = 10
d["b"] = 20

# Update existing key
d["a"] = 100

print(d)


# =====================================================
# POINT 9: REMOVING ELEMENTS
# =====================================================

d = {"a": 1, "b": 2, "c": 3}

# pop() – removes by key
print(d.pop("a"))            # 1

# pop() safe version
print(d.pop("x", None))      # None

# popitem() – removes LAST inserted item
print(d.popitem())           # ('c', 3)

# del keyword
del d["b"]

print(d)

# clear()
d.clear()
print(d)                     # {}


# =====================================================
# POINT 10: COPYING DICTIONARIES
# =====================================================

d1 = {"a": [1, 2]}
d2 = d1.copy()               # shallow copy

d2["a"].append(3)

print(d1)                    # {'a': [1, 2, 3]}
print(d2)                    # {'a': [1, 2, 3]}

# Deep copy
import copy
d3 = copy.deepcopy(d1)
d3["a"].append(4)

print(d1)                    # unchanged


# =====================================================
# POINT 11: SETDEFAULT()
# =====================================================

d = {}

# If key exists → return value
# If key does not exist → insert with default
d.setdefault("a", 0)
d.setdefault("a", 100)

print(d)                     # {'a': 0}


# =====================================================
# POINT 12: UPDATE()
# =====================================================

d = {"a": 1}
d.update({"b": 2, "c": 3})
d.update([("d", 4), ("e", 5)])

print(d)# {"a":1,"b":2,"c":3,"d":4,"e":5,}


# =====================================================
# POINT 13: DICTIONARY COMPREHENSION
# =====================================================

squares = {x: x*x for x in range(5)}
even_squares = {x: x*x for x in range(10) if x % 2 == 0}

print(squares)
print(even_squares)


# =====================================================
# POINT 14: NESTED DICTIONARIES
# =====================================================

data = {
    "user": {
        "name": "Rishu",
        "age": 20
    },
    "skills": ["Python", "C"]
}

print(data["user"]["name"])
print(data["skills"][0])


# =====================================================
# POINT 15: IMPORTANT DICTIONARY METHODS
# =====================================================

d = {"a": 1, "b": 2}

print(d.keys())
print(d.values())
print(d.items())
print(len(d))


# =====================================================
# POINT 16: WHAT DICTIONARY IS NOT
# =====================================================

# ❌ No indexing
# d[0]

# ❌ No slicing
# d[1:3]

# ❌ Keys cannot be renamed
# d["a"] → "b"  # invalid


# =====================================================
# POINT 17: PERFORMANCE NOTES
# =====================================================

# Average time complexity:
# Lookup   → O(1)
# Insert   → O(1)
# Delete   → O(1)

# Dictionaries are implemented using HASH TABLES


# =====================================================
# FINAL SUMMARY
# =====================================================

# ✔ dict is mutable
# ✔ keys are unique & hashable
# ✔ values can be anything
# ✔ insertion order preserved
# ✔ fast lookups
# ✔ accessed by keys, not index
