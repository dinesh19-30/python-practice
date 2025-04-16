#keyword arguments= an argument preceded by an identifier help with readablity order of arguments does'nt matter 
#1.positional 2.default 3.keyword 4.arbitrary

#1

def hello(greeting,title,first,last):
    print(f"{greeting} {title} {first} {last}")
hello(title="Hello",greeting="Mr.",last="Dinesh",first="Hariraman")    

#2
#end keyword

for i in range(1,11):
    print(i,end=" ")

#3
#separate keyword

print("1","2","3","4","5",sep="-")

#4

def get_phone(country,first,last):
    return f"{country}-{first}-{last}"
ph=get_phone(country=91,first=90251,last=19360)
print(ph)