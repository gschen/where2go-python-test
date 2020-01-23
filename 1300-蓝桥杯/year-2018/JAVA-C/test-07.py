m=int(input())
n=list(map(int,input().split(' ')))
# print(m,list(n))
l=[]
for i in n:
    x=n[i-1]
    l.append(x)