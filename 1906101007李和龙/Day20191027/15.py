"""

"""
n,m = map(int,input().split("/"))
for i in range(2,n+1):
    if n%i==0 and m%i==0:
        n=n//i
        m=m//i
print(n,"/",m)