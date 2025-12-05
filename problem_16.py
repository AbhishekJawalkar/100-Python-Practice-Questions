# Multipication table

n = int(input("Enter a number whose table you want : "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

# Multiplication table till the number

m = int(input("Enter a number till whom you want tables : "))
for i in range (1, m+1):
    print(f"Multiplication table of {i}")
    for j in range (1, 11):
        print(f"{i} x {j} = {i*j}")
    print()