#python calculator

op=input("Enter the operator (+ - * / %): ")

num1=float(input("Enter num1: "))
num2=float(input("Enter num2: "))

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2,2)
elif op=="%":
    print(num1%num2)      
else:
    print("invalid input")              