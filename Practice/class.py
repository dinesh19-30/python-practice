class laptop:
    def __init__(self):
        self.price=1000
        self.ram=""
        self.processor=""   
hp=laptop()
hp.price=f"Maximum price :{10000}"
hp.processor="i7"
hp.ram="5gb"
print(hp.price)
print(hp.processor)
print(hp.ram)