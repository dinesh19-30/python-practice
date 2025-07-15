class laptop:
    def __init__(self):
        self.price=1000
        self.ram=""
        self.processor=""  
    def display(self):
        print("ram =",self.ram) 
        print("processor =",self.processor)    
        print(self.price)
hp=laptop()
dell=laptop()
mac=laptop()
hp.price=f"Maximum price :{10000}"
hp.processor="i7"
hp.ram="5gb"

dell.price=f"Maximum price :{20000}"
dell.processor="i7"
dell.ram="5gb"

mac.price=f"Maximum price :{300000}"
mac.processor="i7"
mac.ram="5gb"
hp.display()
dell.display()
mac.display()