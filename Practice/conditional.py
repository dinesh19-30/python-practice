#if statement = a block of code that will execute if its condition is true

age=int(input("age="))
if age==100:
    print("your are a century old")
elif age < 0:
    print("you haven't been born yet")  
elif age>=18:
    print("how old are you: ")     
else:
    print("your are a child")