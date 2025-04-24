#for loop - Execcutes the block of code

#1
for i in range(1,11):
    print(i)
print("HAPPY NEW YEAR")

#2
for i in reversed(range(1,11)):
    print(i)
print("HAPPY NEW YEAR")

#3
for i in range(1,11,2):
    print(i)

#4
for i in range(1,21):
    if i==13:
        continue                #continue key word used for skip the value and continue the loop.
    else:
        print(i)   

#5
for i in range(1,21):
    if i==13:
        break                #break key word used for stop the loop and break it.
    else:
        print(i) 
        
          
