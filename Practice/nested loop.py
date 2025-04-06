#nested loop - a loop within another loop
#1
for x in range(3):
    for y in range(1,11):
        print(y,end="")
    print()    

    #2
    r=int(input("Enter the rows: "))
    c=int(input("Enter the columns: "))
    s=input("Enter the symbol: ")
    for i in range (r):
        for j in range(c):
            print(s,end="")
        print()    