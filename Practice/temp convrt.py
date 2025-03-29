unit=input("is this temperature in celsius or fahrenheit (C/F): ")
temp=float(input("Enter the temp"))

if unit=="C":
    temp=round((9*temp)/5+32, 1)   
    print(f"Temperature in fahrenheit is :{temp} f")
elif unit=='F':
    temp=round((temp-32)*5/9,1)    
    print(f"Temperature in celsiusis is :{temp} c")
else:
    print(f"{unit} is invalid input")    