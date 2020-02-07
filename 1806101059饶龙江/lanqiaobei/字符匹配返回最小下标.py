s=input()
d=list(input())
b=0
for i in s:
    if i in d:
        a = d.index(i)
        del d[0:a]
        b+=a
    else:
        print(-1)
print(b+1)

