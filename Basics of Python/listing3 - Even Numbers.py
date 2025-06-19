n = int(input("Enter the last number: "))
print("0", end="")
for i in range(1, n+1, 2):
    print(", ", end="")
    print(i, end="")