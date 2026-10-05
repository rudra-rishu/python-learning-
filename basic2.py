###LOOPS :- 

# -Python has two main loops:
# 1>for loop
# 2>while loop

## FOR loop- 
# syntax-  for variable in sequence:
#             statements


print("For loop content begins here ")

for i in range(5): 
    print(i,end=" ") 
print()

for i in range(2, 6):
    print(i,end=" ")
print()

for i in range(1, 10, 2): #range(start, stop, step)
    print(i,end=" ")
print()

for i in range(10, 1, -1): #range(start, stop, step) this is the reverse of 1 to 10
    print(i,end=" ")
print()

# over strings
for ch in "python":
    print(ch,end=" ")
print()


## WHILE Loop
# syntax - while condition:
#             statements


print("while loop content begins here ")
i = 1
while i <= 5:
    print(i,end=" ")
    i += 1
print()

s = "python"
i = 0
while i < len(s):
    print(s[i], end=" ")
    i += 1
print()

## ELSE in loop -

#The else block runs only if the loop finishes normally (i.e., no break happened)
print("ELSE in loop starts here ")

s = "python"

for ch in s:
    if ch == "z":
        print("Found")
        break
else:
    print("Not found")
print()

## enumerate()
# this gives index + value together

print("enumerate() in loop start here")

names = ["Alice", "Bob", "Charlie"]
for i, name in enumerate(names):
    print(i, name,end=" " )

print()

for i, item in enumerate(["pen", "book", "eraser"], start=1):
    print(f"{i}. {item} ",end=" ")
print()

## ZIP()
# it is used to loop over multiple sequences in parallel 

print("zip () in loop  starts here ")
names = ["Alice", "Bob"]
marks = [85, 90]

for name, mark in zip(names, marks):
    print(name, mark)

print()

a = [1, 2, 3, 4]
b = ["x", "y"]

for i, j in zip(a, b):
    print(i, j) # zip() stops at the shortest iterable when there are unequal length of sequences

###-----








