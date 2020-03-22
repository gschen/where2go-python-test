class Test:
    def __init__(self):
        self.x=[1,2,3]
a = Test()
a.x.append('123')
b = Test()
print(a.x)
print(b.x)
