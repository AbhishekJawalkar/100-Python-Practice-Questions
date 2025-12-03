# Swap two Variables

# INPUT
# Two methods
# Method - 1 - Using 3rd Variable
print("Method - 1 - Using 3rd Variable")
print()
a = 10
b = 5
c = a
a = b
b = c
print(a)
print(b)
print()

# Method - 2 - Without Using 3rd Variable
print("Method - 2 - Without Using 3rd Variable")
print()
a = 10
b = 5
a,b = b,a
print(a)
print(b)


# OUTPUT
# Method - 1 :- a = 5, b = 10
# Method - 2 :- a = 5, b = 10