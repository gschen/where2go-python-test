# n=int(input())
# l=[x for x in range(n)]
# while n>1:
#     if n%3

def ysf(n):
    l=list(range(1,n+1))
    x=0
    for i in range(n-1):
        x=(x+3)%len(l)-1
        l.pop(x)
    return l[0]
print(ysf(10))