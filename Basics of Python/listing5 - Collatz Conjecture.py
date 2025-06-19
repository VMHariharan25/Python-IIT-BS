# Collatz Conjecture 

n = int(input("Enter a Number: "))
loop = 0
print(f"The Collatz Sequence is \n{n} ", end = '')
while(n != 1):
    if(n%2 == 0):
        n = n // 2 
    else: 
        n = 3*n + 1 
    loop = loop + 1
    print(f"{n} ", end = '')

print(f"\nTotal number of times the loop run = {loop}")
