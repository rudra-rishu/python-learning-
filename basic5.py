# =====================================================
# POINT 1: WHAT IS A LIST?
# =====================================================

#A Python list is an object that owns a contiguous array of references, and each reference points to a separate object in the heap.
# the elements of the list are mutable 
# It can store duplicate values and mixed data types 
# HEAP MEMORY
# ────────────────────────────────────────────────────────────

# List Object (PyListObject)
# ┌──────────────────────────────────────────|
# │ ob_refcnt                                |                
# │ ob_type|                                 |
# │ ob_size = 3                              │               
# │ ob_capacity = 4                          │               
# │ ob_item  ───────────────--               │               
# └──────────────────────────| ──────────────┘              
#                            │                                
#                            ▼                                
#           CONTIGUOUS BLOCK OF REFERENCES (POINTER ARRAY)    
#           (owned & managed by the list object)              
#           ┌──────────┬──────────┬──────────┬──────────┐   
#           │  ref[0]  │  ref[1]  │  ref[2]  │  unused  │   
#           └──────────┴──────────┴──────────┴──────────┘   
#                │            │            │                 
#                ▼            ▼            ▼                 
#              int 10       str "hi"      float 3.14          
#             (object)     (object)       (object)            


lst = [1, 2, 3, "hello", 3.5, True]

print(lst)
print(type(lst))            # <class 'list'>


# =====================================================
# POINT 2: CREATING LISTS
# =====================================================

# Empty list
a = []

# List with elements
b = [10, 20, 30]

# Mixed data types
c = [1, "python", 3.14, False]

print(a)
print(b)
print(c)

# Creating list from other sequences
print(list("python"))       # ['p', 'y', 't', 'h', 'o', 'n']
print(list(range(5)))       # [0, 1, 2, 3, 4]


# =====================================================
# POINT 3: ORDERED COLLECTION (INDEX-BASED)
# =====================================================

nums = [10, 20, 30, 40]

# Order is preserved
print(nums[0])              # 10
print(nums[1])              # 20
print(nums[-1])             # 40

# Order matters
print([1, 2, 3] == [3, 2, 1])   # False


# =====================================================
# POINT 4: INDEXING & SLICING
# =====================================================

nums = [10, 20, 30, 40, 50]

# Indexing
print(nums[2])              # 30

# Slicing: start : end : step
print(nums[1:4])            # [20, 30, 40]
print(nums[:3])             # [10, 20, 30]
print(nums[2:])             # [30, 40, 50]
print(nums[::-1])           # [50, 40, 30, 20, 10]

# Slicing is safe
print(nums[0:100])          # full list


# =====================================================
# POINT 5: LISTS ARE MUTABLE
# =====================================================

nums = [1, 2, 3]

# Modify element
nums[0] = 100
print(nums)                 # [100, 2, 3]

# Modify slice
nums[1:3] = [9, 8]
print(nums)                 # [100, 9, 8]


# =====================================================
# POINT 6: LOOPING / TRAVERSAL
# =====================================================

nums = [10, 20, 30]

# Element-based loop
for x in nums:
    print(x)

# Index-based loop
for i in range(len(nums)):
    print(i, nums[i])

# Best way: enumerate
for i, val in enumerate(nums):
    print(i, val)


# =====================================================
# POINT 7: MEMBERSHIP OPERATORS
# =====================================================

nums = [1, 2, 3, 4]

print(2 in nums)            # True
print(5 not in nums)        # True


# =====================================================
# POINT 8: ADDING ELEMENTS
# =====================================================

nums = [1, 2, 3]

# append() -> add ONE element
nums.append(4)
print(nums)                 # [1, 2, 3, 4]

# extend() -> add multiple elements
nums.extend([5, 6])
print(nums)                 # [1, 2, 3, 4, 5, 6]

# insert() -> add at index
nums.insert(1, 100)
print(nums)                 # [1, 100, 2, 3, 4, 5, 6]


# =====================================================
# POINT 9: REMOVING ELEMENTS
# =====================================================

nums = [10, 20, 30, 40]

# remove() -> remove by value
nums.remove(20)
print(nums)                 # [10, 30, 40]

# pop() -> remove by index (returns value)
x = nums.pop()
print(x)                    # 40
print(nums)                 # [10, 30]

# del -> delete by index or slice
del nums[0]
print(nums)                 # [30]


# =====================================================
# POINT 10: REMOVE() vs DEL
# =====================================================

nums = [1, 2, 3, 2]

nums.remove(2)              # removes first occurrence
print(nums)                 # [1, 3, 2]

nums = [1, 2, 3, 4]
del nums[1:3]               #using del we can remove slice of elements - which is not possible in pop() and remove()
print(nums)                 # [1, 4]


# =====================================================
# POINT 11: SEARCHING & COUNTING
# =====================================================

nums = [10, 20, 30, 20]

print(nums.index(20))       # 1
print(nums.count(20))       # 2


# =====================================================
# POINT 12: SORTING & REVERSING
# =====================================================

nums = [4, 1, 3, 2]

# sort() -> modifies list   #uses timsort internally to sort , also the default sorting is done in ascending order
nums.sort()
print(nums)                 # [1, 2, 3, 4]

nums.sort(reverse=True)     #internally the sorting is done in ascending order only , just the order is reversed using reverse=true
print(nums)                 # [4, 3, 2, 1]

# sorted() -> returns new list  : it also uses tim sort and the default order of sorting is ascending 
nums = [4, 1, 3, 2]
new_nums = sorted(nums)
print(new_nums)
print(nums)                 # unchanged

# reverse() -> reverse order
nums.reverse()
print(nums)


# =====================================================
# POINT 13: SORTING WITH KEY (LAMBDA)
# =====================================================


# data.sort(key=...) --> this in python basically means  that - for each element in the list compute a value and use  that  value to decide the  sorting order 

#key = lambda element: value_to_sort_by


data = [(1, 3), (4, 1), (2, 2)]

# Sort by second element
data.sort(key=lambda x: x[1]) # lamda is a anonymous function , x is the element of the list ,x[1] is the second element of x . so basically, we are saying that the value of the key is the 2nd element of a element of a list . hence, we are telling to the sort() to sort the  list in ascending order corresponding to the 2nd element of a element of the list 
print(data)                 # [(4, 1), (2, 2), (1, 3)]

students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 95},
    {"name": "C", "marks": 70}
]

students.sort(key=lambda s: s["marks"]) # here the value of the key is marks key of the dictonary , thus sorting will be done in the ascending order corresponding to the marks key of the dictonary .  
print(students)

## keys can also be used with sorted() eg:
x=sorted(data,key=lambda x: x[0])
print(x)

# sorting using length of a string 
words = ["python", "c", "java"]
words.sort(key=len)
print(words)


# =====================================================
# POINT 14: COPYING LISTS (VERY IMPORTANT)
# =====================================================

a = [1, 2, 3]

# ❌ Wrong (aliasing)
b = a
b[0] = 100
print(a)                    # [100, 2, 3]

# ✅ Correct copies
a = [1, 2, 3]
b = a.copy()
c = a[:]
d = list(a)

b[0] = 999
print(a)                    # [1, 2, 3]


# =====================================================
# POINT 15: NESTED & 3D LIST TRAVERSAL
# =====================================================

matrix = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

for layer in matrix:
    for row in layer:
        for value in row:
            print(value)


# =====================================================
# POINT 16: LIST COMPREHENSION
# =====================================================

# list comprehension : A compact syntax for creating lists from loops


# Basic
squares = [x*x for x in range(5)]
print(squares) #[0,1,2,3,4]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Flatten nested list
flat = [x for row in [[1,2],[3,4]] for x in row]
print(flat)


# =====================================================
# POINT 17: LIST AS STACK (LIFO)
# =====================================================

stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())          # 3
print(stack)                # [1, 2]


# =====================================================
# POINT 18: WHY LIST IS BAD FOR FIFO
# =====================================================

queue = [1, 2, 3]

# ❌ Slow (O(n))
queue.pop(0)
print(queue)


# =====================================================
# POINT 19: CORRECT TOOL FOR FIFO (deque)
# =====================================================

from collections import deque # collection.deque is a special data structire in python for FIFO

q = deque()
q.append(1)
q.append(2)
q.append(3)

print(q.popleft())          # 1
print(q)                    # deque([2, 3])


# =====================================================
# POINT 20: BUILT-IN FUNCTIONS WITH LISTS
# =====================================================

nums = [1, 2, 3, 4]

print(len(nums))            # 4
print(sum(nums))            # 10
print(max(nums))            # 4
print(min(nums))            # 1

print(any([0, 0, 5]))       # True - checks for any true value among the elements
print(all([1, 2, 3]))       # True - checks if all the values in  the list is true or not 

print(list(reversed(nums))) # [4, 3, 2, 1]

names = ["A", "B", "C"]
marks = [90, 80, 70]

print(list(zip(names, marks)))

for i, val in enumerate(nums):
    print(i, val)


# =====================================================
# POINT 21: PERFORMANCE NOTES (IMPORTANT)
# =====================================================

# append() -> O(1) amortized
# index access -> O(1)
# insert/remove in middle -> O(n)
# pop(0) -> O(n)

# Lists store CONTIGUOUS REFERENCES, not objects
# That is why indexing is fast, but shifting is slow
