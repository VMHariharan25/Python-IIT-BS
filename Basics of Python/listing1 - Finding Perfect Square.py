# Finding where a number is a perfect square
num = int(input("Enter a Number: "))

if( (int(num**0.5)**2) == num ):
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")