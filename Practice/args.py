#*args=allows you to pass multiple non key arguments
#*kwargs=allows you to pass multiple keyword arguments
#1. postional 2.default 3.keyword 4.arbitrary

#1

def add(*nums):
    total=0
    for num in range(1,11):
        total +=num
    return total
print(add())  

#2

def display(*args):
    for arg in args:
        print(arg,end=" ")
display("Mr.","Dinesh","you","are","amazing.")        

