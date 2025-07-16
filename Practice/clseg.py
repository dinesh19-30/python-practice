class Person:
    def __init__(self,n,age,loc):
        self.n=n
        self.age=age
        self.loc=loc
    def display(self):
        print(f"{self.n} {self.age} {self.loc}")
n=input()
a=int(input())
l=input()
p=Person(n,a,l)
p.display()