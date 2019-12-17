l=list(input().split())
s=[]
for a in l:
    a=int(a)
    s.append(a)
s.sort()
print('%d->%d->%d' % (s[0],s[1],s[2]))
