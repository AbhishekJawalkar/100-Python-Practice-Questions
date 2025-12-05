# Temperature converter

print("-"*50)
print("\n")

input_temp = float(input("Enter the temperature in number ( eg - 33) : "))
print("\n")

input_type = input("Enter the type of termperature ( c = Celsius / f = Fahrenheit / k = Kelvin ) : ").lower()

c = "c"
f = "f"
k = "k"
print("\n")

output_type = input("Enter the type of termperature you want to be converted into (c = Celsius/ f = Fahrenheit/ k = Kelvin) : ").lower()
print("\n")

if input_type == c and output_type == f :
    print(f"Converted temperature : {(input_temp * 9/5) + 32} F")
elif input_type == c and output_type == k :
    print(f"Converted temperature : {input_temp + 273.15} K")
elif input_type == f and output_type == c :
    print(f"Converted temperature : {(input_temp - 32) * 5/9} C")  
elif input_type == f and output_type == k :
    print(f"Converted temperature : {((input_temp - 32) * 5/9) + 273.15} K")
elif input_type == k and output_type == c :
    print(f"Converted temperature : {input_temp - 273.15} C")
elif input_type == k and output_type == f :
    print(f"Converted temperature : {((input_temp - 273.15) * 9/5) + 32 } F")
else:
    print("Something went wrong")
    
print("\n")
