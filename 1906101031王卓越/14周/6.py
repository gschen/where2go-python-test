#不用set()函数来解决第1题
l=map(int,input().split())
l=list(l)
s=[]
for a in range(len(l)):
    for b in range(len(l)):
        if a!=b and l[a]==l[b] and b<a:
            s.append(l[b])
l.reverse()
for k in s:
    l.remove(k)
l.reverse()
print(l)

