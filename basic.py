#  VARIABLE BASICS --

x = 10
x = "hello"
print(x)
# python is dynamically type , also it do not need data type declaration
student_name = "Rishu"
total_marks = 480
print(student_name,total_marks)
# when using 2 word variable - use Snake_case 
PI = 3.14
MAX_LIMIT = 100
print(PI,MAX_LIMIT ) #comma automatically adds space in between 
# constant should be all caps
name = "Rishu"
age = 20
print( f"My name is {name} and I am {age} years old.")
# this is the best pracrice to embed variable in a string while printing 


#---

# TAKING VALUE FROM USERS --

x = input("what is your name  :")
print(x)

input_str = input("Which year were you born? ")
year = int(input_str)
print(f"Your age at the end of the year 2021: {2025 - year}" )

height = float(input("What is your height? "))
weight = float(input("What is your weight? "))

height = height / 100
bmi = weight / height ** 2

print(f"The BMI is {bmi}")

#---

# CONDITIONALS ---
 
#In python - indentation marks that a code belongs to a block - so while using if , else and elif - we must indenatate the  code when wan to put in the block of a conditional statement . ALSO PUT : AT THE END FO THE CONDITOONAL STATEMENT

#COMPARISON OPERATORS- with correct order of precedance 
	
# >	    greater than	
# <	    less than	
# >=	greater or equal
# <=	less or equal
# ==	equal to	
# !=	not equal

#LOGICAL OPERATOR - with correct order of precedance 
# not 
# and 
# or 

# COMPARISON OPERATOR > LOGICAL OPERATOR - precedance  order 


age = 17
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(status)


marks = 75
if (marks >= 90): # () are allowed in python but they are not required 
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


#ternery operator- 
age = 17
status = "Adult" if age >= 18 else "Minor"
print(status) #this  is ternarty operator - synatx :value_if_true if condition else value_if_false

# how ()can be helpfull
age =25 
has_id= True
is_vip=False
if (age >= 18 and has_id) or is_vip:# this is were () can be helpfull
     print("Allowed")  


#comparing string with non string

#correct way - 
print(int("10") > 5)   # because in python with comparing strings with non string only explicit conversion is required .

#incorrect way - print("10" > 5) : because implicity type conversion in not allowed in python 


#---












