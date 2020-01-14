from functools import *
def raw(x,y):
    return 10*x+y
a,n=map(int,input().split())
s=[]
k=0
for i in range(n):
    s.append(a)
    k=k+reduce(raw,s)
print(k)    




