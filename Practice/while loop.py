#while loop = execute some code while condition is true
#1
name=input("Enter your name")
while name=="":
    print("you did not enter your name")
    name=input("Enter your name")
print(f"Hello {name}")    

#2
age=int(input("Enter your age : "))
while age<0:
    print("Age cant be negative")
    age=int(input("Enter your age : "))  
print(f"you are {age} years old")    

#3
food=input("Enter your food you like (q to quit) : ")
while not food=="q":
    print(f"you like {food}")    
    food=input("Enter another food you like (q to quit): ")
print("bye")

#4
num=int(input("Enter a num between 1 to 10 "))
while num<1 or num>10:
    print(f"{num} is not valid")
    num=int(input("Enter a num between 1-10: "))
print(f"your number is {num}")