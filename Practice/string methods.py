#1

name=input("Enter your name: ")
ph_no=input("Enter your ph no: ")

result=len(name)
print(result)

result1=name.find(" ")
print(result1)

result2=name.rfind("n")
print(result2)

result3=name.capitalize()
print(result3)

result4=name.upper()
print(result4)

result5=name.lower()
print(result5)

result6=name.isdigit()
print(result6)

result7=name.isalpha()
print(result7)

result8=ph_no.count("-")
print(result8)

result9=ph_no.replace("-"," ")
print(result9)