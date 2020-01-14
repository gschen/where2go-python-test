class test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add_(self,a,b):
        print(self.a+self.b)
    def reduce_(self,a,b):       
        print(self.a-self.b)
n=test(1,5)
n.add_(1,2)
n.reduce_(1,5)


