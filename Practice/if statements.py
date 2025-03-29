#1
response=input("Would you food? (Y/N)")
if response=="Y":
    print("food available for you")
else:
    print("food not available for you")    

#2
name=input("Enter your name:")
if name=="":
    print("you did not type in your name")
else:
    print(f"HELLO {name}") 

#3
for_sale=True
if for_sale:
    print("product for sale") 
else:
    print("products not for sale")  

#4
online=False
if online:
    print("you are online") 
else:
    print("you are offline")                