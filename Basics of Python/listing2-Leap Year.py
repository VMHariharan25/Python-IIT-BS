# Finding a Leap Year 
"""
General Ideology: 
    If a year is divisible by 4, it is a leap year.
    Postive Example: 2020 is a leap year
    Negative Example: 1800 is not a leap year; 1800 is divisible by 4 but not a leap year.

    Original Rule: 
        1. If a year is divisible by 400, it is a leap year. (Century years like 1600, 2000, etc. are leap years)
        2. If a year is divisible by 4, it is a leap year. (non Century years like 2020, 2024, etc. are leap years)
"""

year = int(input("Enter a Year: "))

"""Version 1
if(year % 100 == 0):
    if(year % 400 == 0): 
        print(f"{year} is a leap year.")
    else: 
        print(f"{year} is not a leap year.")
elif(year % 4 == 0): 
    print(f"{year} is a leap year.")
else: 
    print(f"{year} is not a leap year.")
""" 
"""
Version 2
if((year % 100 == 0) and (year % 400 == 0)): 
    print(f"{year} is a leap year.")
elif((year % 100 != 0) and (year % 4 == 0)):
    print(f"{year} is a leap year.")
else: 
    print(f"{year} is not a leap year.")
"""

""" Version 3
if(((year % 100 == 0) and (year % 400 == 0)) 
        or ((year % 100 != 0) and (year % 4 == 0))): 
    print(f"{year} is a leap year.")
else: 
    print(f"{year} is not a leap year.")
"""

# Flag based Computation Thinking 

"""
Ternary Operator: (Orginated C Programming)
a = b? c : d; 
"?:;" --> Ternary Operator 
Interpretation: If the Expression b is True, then a is assigned with c else a is assigned with d 

Python Style: 
x = True_block if condition else False_Block 
"""
"""Version 4
leap_year = True if(((year % 100 == 0) and (year % 400 == 0)) or ((year % 100 != 0) and (year % 4 == 0))) else False 
print(f"{year} is {'not ' if(not leap_year) else ""}a leap year.")
"""

print(f"{year} is {"" if(((year % 100 == 0) and (year % 400 == 0)) or ((year % 100 != 0) and (year % 4 == 0))) else "not "}a leap year.")