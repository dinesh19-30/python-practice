#python CI calculator

p=0
r=0
t=0
while p<=0:
    p=float(input("Enter the principal amount: "))
    if p<=0:
        print("principal amount can't be less than zero")
print(p)

while r<=0:
    r=float(input("Enter the rate: "))
    if r<=0:
        print("rate can't be less than zero")
print(r)

while t<=0:
    t=float(input("Enter the time: "))
    if t<=0:
        print("time can't be less than zero")
print(t)

total=p*pow((1+r/100),t)

print(f"Balance after {t} year/s: {total:.2f}")