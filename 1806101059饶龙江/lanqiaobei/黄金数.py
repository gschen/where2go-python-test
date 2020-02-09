a=1
b=3
s=a/b
while round(s*1000000)/1000000!=0.618034:
    a,b=b,a+b
    s=a/b
    S=str(a)+'/'+str(b)
print(S)




