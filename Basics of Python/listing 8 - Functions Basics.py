## Functions in Python
"""
1. Function definition: 
def function_name(parameters):
    # function body
    return value

2. Function call:
function_name(arguments)

Types of functions:
- Built-in functions: print(), len(), type(), etc.
- User-defined functions: Functions created by the user for specific tasks.
"""
def sum_fn(a,b): # parameters 
    c = a + b 
    print("Addition of two numbers is " + str(c))

p = int(input("Enter p: "))
q = int(input("Enter q: "))
sum_fn(p,q) # Arguments 
## Number of arguments = number of parameters 
