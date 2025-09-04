
from itertools import product

t1, t2 = (1, 4), (3, 9)

print("First tuple :", t1)
print("Second tuple :", t2)

comb = list(product(t1,t2)) + list(product(t2,t1))
print("All pair Combinations are:", comb)
