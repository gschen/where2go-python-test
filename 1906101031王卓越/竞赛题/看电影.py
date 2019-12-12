N,K=map(int,input('请输入：').split())
l=input().split()
a=2
s=l[:K]
while a<N:
    if a>=K:
        for b in s[-K:]:
            if a>=N:
                break
            if b==l[a] and a<N:
                a=a+1
                continue
            elif s[-1]!=l[a] and a<N:
                s.append(l[a])
                print(s)
                a=a+1
                continue
print(K)
print(' '.join((s[-K:])))
