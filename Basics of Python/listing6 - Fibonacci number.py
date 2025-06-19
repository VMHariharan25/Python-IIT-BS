# Fibannacci Numbers 
# 1 1 2 3 5 8 13 21 
n = int(input("Enter the number of terms: "))
k = m = 1 
print(f"Fibanacci Sequence: {k} {m} ", end='')
for i in range(1, n-1):
    print(f"{k + m} ", end='')
    temp = k 
    k = m
    m = temp + k

