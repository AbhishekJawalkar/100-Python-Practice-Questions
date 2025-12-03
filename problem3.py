# Find & Calculate the Square root of a number

# INPUT
# Two methods
# Method 1 - Using Exponentiation
print("----------SQUARE ROOT FINDER----------")
print()
print("Method 1 - Using Exponentiation")
print()
num1 = int(input("Enter a Number : "))
square_root_1 = num1 ** (1/2)
print("Square root is :", square_root_1)

# Method 2 - Using Math Module
print()
print("Method 1 - Using Math Module")
print()
import math
num2 = int(input("Enter a Number : "))
square_root_2 = math.sqrt(num2)
print("Square root is :", square_root_2)