def raw(k):
    s=[]
    for u in k:
        s.append(u)              
    s.reverse()
    return (''.join(s))
p=[]
n=input('请输入字符串：')
for a in range(len(n)+1):
        for b in range(len(n)+1):
            k=n[b:a]
            if k==raw(k):
                p.append(k)
print(max(p))