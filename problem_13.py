# Prime numbers in an interval

lower_interval = int(input("Enter the Starting number : "))
upper_interval = int(input("Enter the Ending number : "))

print("Prime Numbers in the given interval are : ", end="")
for n in range(lower_interval,upper_interval + 1):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            print(n, end=" ")
      