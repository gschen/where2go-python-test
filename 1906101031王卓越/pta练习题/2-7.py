from functools import*
def raw(x,y):
    return 10*x+y
A,B=map(int,input().split(','))
s=[]
k=0
for i in range(B):
    s.append(A)
print(reduce(raw,s))


