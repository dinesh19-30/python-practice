#type casting = conver the data type of a value to another data type

x=1
y=2.0
z="3"

z=str(z)
x=str(x)
y=str(y)

print(x)
print(y)
print(z*3)

name=input("what is your name: ")
age=int(input("how old are you: "))
height=float(input("How tall are you: "))
age=age+1
print("hello "+name)
print("you are "+str(age)+"year old")
print("your are "+str(height)+"cm tall")