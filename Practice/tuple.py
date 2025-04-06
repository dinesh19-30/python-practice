#set - () ordered and unchageable. Duplicates ok. faster

fruits=("apple","orange","grapes","banana","banana")
print(fruits)
#print(dir(fruits))
#print(help(fruits))
print(fruits.index("apple"))
print(fruits.count("banana"))
#fruits.remove("apple")
#fruits.pop()
#fruits.clear()
print(fruits)

for fruit in fruits:
    print(fruit)