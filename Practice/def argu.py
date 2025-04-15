import time

def count(e,s=0):
    for i in range(s,e+1):
        print(i)
        time.sleep(1)
    print("Done!")    

print(count(30,15 ))