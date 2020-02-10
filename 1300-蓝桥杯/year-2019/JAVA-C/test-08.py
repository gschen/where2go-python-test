N=2
M=6
T=6
a=[1,1,5,2,3,1,6,2,2,1,6,2]
s=[]
n=0
for i in range(0,len(a),2):
    s.append(a[i:i+2])
for i in range(1,N+1):
    x=[]
    for ii in range(len(s)):
        if i==s[ii][-1]:
            x.append(s[ii][0])
    x.sort()
    y=len(x)*2#6
    for i in range(len(x)-1):
        b=x[i+1]-x[i]
        if b<=1:
            pass
        else:
            y=y-(b-1)
    y=y-(T-x[-1])
    if y>5:
        n+=1
print(n)
