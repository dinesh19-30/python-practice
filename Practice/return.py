#return= statement used to end a function and send a result back to the caller

def add(x, y):
    z=x+y
    return z

def sub(x, y):
    z=x-y
    return z

def mul(x, y):
    z=x*y
    return z

def div(x, y):
    z=x/y
    return z

print(add(1, 2)) 
print(sub(1, 2))
print(mul(1, 2))
print(div(1, 2))   

#2

def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first + " " + last
f_name=create_name("dinesh","hariraman")

print(f_name)