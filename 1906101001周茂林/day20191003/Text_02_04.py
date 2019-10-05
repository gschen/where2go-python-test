a,n = map(int,input().split())
i = 1
s = 0
while i <= n:
    b = int(i * str(a))
    s +=b
    i = i+1
print(s)