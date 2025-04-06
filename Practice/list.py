#List - [] ordered and changeable. Duplicates ok.

fruits=["apple","orange","grapes","orange"]
fruits[0]="pine apple"
print(fruits)
print(fruits[::-1])

for fruit in fruits:
    print(fruit)

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)
print("pine apple" in fruits)

fruits.append("pine apple")
fruits.remove("pine apple")
fruits.insert(0,"pine apple")
fruits.sort()
fruits.reverse()
fruits.clear()

