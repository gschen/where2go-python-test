N=5
a=[2,6,4,10,20]
a.sort()
s=[]
for i in range(len(a)-1):
    x=a[i+1]-a[i]
    s.append(x)
print(len(list(range(a[0],a[-1]+1,min(s)))))
