#set - {} unordered and immutable, but add/remove ok. no duplicates 

fruits={"apple","orange","grapes","banana","banana"}
print(fruits)
#print(dir(fruits))
#print(help(fruits))

fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()
fruits.clear()
print(fruits)