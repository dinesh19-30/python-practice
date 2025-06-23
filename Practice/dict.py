#dictionary - a collection key and values pairs.ordered and changeable.no duplicates
#syn= {key:value}

cap={"INDIA":"new delhi",
     "USA":"washington",
     "china":"beijing",
     "japan":"moscow"}
print(dir(cap))
print(help(cap))
print(cap.get("japan"))

for caps in cap:
    print(caps,end=" ")

if cap.get("japan"):
       print("The capital is exist")
else:
    print("The capital does not exist")

cap.update({"INDIA":"Detroit"})  
cap.pop("china")
print(cap)
cap.popitem
print(cap)
