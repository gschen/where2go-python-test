from functools import *
def raw(x,y):
    return x*y
def jkl(x,y):
    return x+y 
n=list(input())
s=[]
for i in n:
    s.append(int(i))
    print(s)
a=reduce(raw,s)
b=reduce(jkl,s)
print(a-b)



