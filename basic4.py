# FUNCTIONS
# def function_name(parameters):  {SYNTAX}
#     # function body
#     return value

#_-----------------------------------
## defining VS calling
def say_hi():      # defining
    print("Hi")

say_hi()           # calling
#-----------------------------------
## parameters VS arguments
def add(a, b):     # parameters
    return a + b

add(5, 10)         # arguments

#----------------------------------
## Multiple return values:
def calc(a, b):
    return a + b, a - b, a * b 

s, d, m = calc(10, 5)

#-----------------------------------
## Default parameters
def greet(name="Guest"):
    print(f"Hello {name}")

greet()
greet("Rishu")

# RULE- Defaults must come after non-defaults so def f(a=10, b):   # ERROR
#-------------------------------------

## Positional arguments :Arguments that are matched to parameters by position (order).

def add(a, b):
    print(a + b)

add(2, 3)
# here :2 goes to a and 3 goes to b Because of position, not name.

add(3, 2)   # different result if order changes

#-----------------------------------

## Keyword arguments : Arguments passed using parameter names.

def profile(name, age):
    print(name, age)

profile(age=20, name="Rishu")

# here :Order does not matter,Python matches by name

#-------------------------------------
## shit to learn later :*awargs, *kwargs , argument order, type hints,Lambda functions,Functions are objects,Higher-order functions,Nested functions,Closures
