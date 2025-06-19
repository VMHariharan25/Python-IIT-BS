# June 9, 2025
# Addition of Three Numbers 
print(5+2+3)

''' 
    Execution of complex Expression 
    for understanding 
'''
print(5 + 2 * 3 - 4 / 2)

"""
>>> x = 5.6
>>> type(x)
<class 'float'>

>>> y = '5.6'
>>> type(y)
<class 'str'>


"""

"""
IMPORTANT NOTE: INDENTATION IS CRUCIAL IN PYTHON
# Indentation Example
>>>  x = 1
  File "<stdin>", line 1
    x = 1
IndentationError: unexpected indent

"""

x = 5 
print(type(x)) 

# June 10, 2025
"""
id(variable) returns the memory address of the variable

>>> x = 7.5
>>> type(x)
<class 'float'>
>>> id(x)
2739537423472
"""

x = y = z = 10 


"""
Integer Division 
"//" is used for integer division in Python, which discards the fractional part.

>>> x = 5
>>> x / 2
2.5
>>> x // 2
2
>>> 22/7
3.142857142857143
>>> 22//7
3
>>> -1//2
-1
>>> -(1//2)
0
"""


"""
Remainder Operation: 
The modulus operator "%" is used to find the remainder of a division operation.
>>> 22 % 7
1

"""


"""
Power Operation:
>>> 2 ** 3
8
>>> 2 ** 3 + 1
9
"""

"""
Boolean Data Type:
>>> x = True
>>> x
True
>>> type(x)
<class 'bool'>
>>> x = False

Boolean Operations:
>>> True and True
True
>>> True and False
False
>>> False and False
False
>>> False and True
False
>>> True or True
True
>>> True or False
True
>>> False or False
False
>>> False or True
True
>>> not True
False
>>> not False
True
"""

### Addition of Two Numbers 


# User Input:  input() function is used to take input from the user.
# Output of Input is always a STRING 

# Current Case: String to Integer Conversion: int() -> Arguments are converted to integers
"""
>>> int('5')
5
>>> int(5.7)
5
>>> int(-2.5)
-2
"""

### Argument: Things given in a function call
### Parameter: Things defined in a function definition

x = int(input("Enter a number: "))  # Taking input from the user and converting it to an integer
y = input("Enter another number ") 
y = int(y) 

sum = x + y 

# Print 1 
print(sum)

# Print 2 
print("The sum of two numbers is:", sum)

# Print 3
print("The sum of two numbers is: " + str(sum))  
# str() is used to convert the integer sum to a string

# Print 4
print(f"The sum of {x} and {y} is: {sum}")

"""
>>> print("Hello World")
Hello World
>>> print("Hello " + "World") # + -> Concatination of Strings 
Hello World
>>> print("Hello", "World", 5) # mixed Data Types you have use commas to separate them 
# While Using commas, Python automatically adds a space between the items
Hello World 5
>>> print("Hello" + "World")
HelloWorld
>>> print("Hello","World",5)
Hello World 5
>>> print("Hello  ","World",5)
Hello   World 5
"""


""" String Formatting:
Type Specifiers in Python:
%d - Integer
%s - String
%f - Float
%c - Character

>>> "%s"%"Hello"
'Hello'
>>> "%d"%6
'6'
>>> "%d %d"%(6,7)
'6 7'
>>> "%d - %d"%(6,7)
'6 - 7'
>>> "%d -"%(6,7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not all arguments converted during string formatting

>>> print("%s %s %d"%("Hello", "World", 5))
Hello World 5
"""

""" F Strings 
h = "Hello"
w = "World"
print(f"{h} {w} {5}") 

"""

# 12 June 2025
"""
>>> # Relation Expression
>>> x = 5
>>> # Inequalities based
>>> x < 10
True
>>> # Relational Expression output: True or False
>>> x < 5
False
>>> x <= 5
True
>>> x
5
>>> x = 10
>>> x
10
>>> x == 10
True
>>> x == 5
False
>>> x != 5
True  
>>> x != 5
True
>>> 1 or 1
1
>>> 0 or 1
1
>>> 0 or 0
0
>>> 1 and 1
1
>>> 1 and 0
0
>>> # x is in the interval (0, 20]
>>> (0 < x) and (x <= 20)
True
>>> 0 < x <= 20
True

On using non zero value in Relation expression, it is considered as True
"""

"""
Conditional Statements:
Syntax: 
if(condition):
    # Code to execute if condition is True
else:
    # Code to execute if condition is False

"""

# Finding the maximum of two numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if x > y:
    print(f"{x} is greater than {y}")

""">>> if( x > y ):
...     print(f"{x} is greater")
...
>>> if x > y:
...     print(f"{x} is greater")
... else:
...     print(f"{y} is greater")
...
20 is greater"""

# if-elif statements
"""
syntax: 
if(condition1):
    # Code to execute if condition1 is True
elif(condition2):
    # Code to execute if condition2 is True
else:
    # Code to execute if both conditions are False
"""

# Finding the maximum of three numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x > y and x > z:
  print(f"{x} is the greatest")
  x = x + 1 
elif y > x and y > z:
    print(f"{y} is the greatest") 
    y = y + 1
else:
      print(f"{z} is the greatest")
      z = z + 1


# June 16 
"""
>>> # Range Object :- Sequence of values
>>> # Syntax: range(start Value, End Value, step = n) 
>>> # Start Value is optional Default:= 0
>>>
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> # End Value is Mandatory
>>> # step is also optional
>>>
>>>
>>> r = range(5)
>>> r
range(0, 5)
>>> type(range(r))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'range' object cannot be interpreted as an integer
>>> type(r)
<class 'range'>
>>> # To convert the range to visible structure list is used. So, list() function is used
>>> # list(range())
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> # range(n) => 0, 1, 2, 3, ... , n-1
>>> # range(n,m) ==> n , n+1, n+2 , ..., m-1
>>> list(range(1,10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(4,5))
[4]
>>> # step is optional but default is 1
>>> list(range(2, 120, 2)
... )
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118]
>>> list(range(2, 120, 3))
[2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119]
>>>
"""

"""
LOOPING: 
Certian statement executed for predefined number of times 
1. for Loop 
Syntax: 

for variable in iterable: 
    loop body 

"""
