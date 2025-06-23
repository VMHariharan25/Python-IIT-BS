# Factorial of a number 

p = int(input("Enter n: "))
"""
fact = 1 
for i in range(2, n+1):
    fact *= i 
"""
def fact(n):
    if(n < 0):
        return 
    elif((n == 1) or (n == 0)):
        return 1 
    else:
        return n*fact(n-1)



print("factorial is", fact(p))