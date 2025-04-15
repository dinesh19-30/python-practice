#default = A default value for certain parameters default is used when argument is omitted make your function more flexible, reduces of #  arguments
# 1. positional 2. DEFAULT 3.keyword 4. arbitrary 

def n_price(l_price,dis=0,tax=0.05):
    return l_price * (1-dis) * (1+tax)
print(n_price(500, 0.1, 0))



