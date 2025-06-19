# X Pattern 
n = int(input("Enter the value of n: "))
for i in range(1, 2*n): 
    for j in range(1,2*n):
        if( (i == j) or (j == 2*n -i)):
            print("*", end = '')
        else:
            print(" ", end = '')
    print("\n", end = '')
